import os
from dotenv import load_dotenv
import tiktoken
from pathlib import Path
from openai import OpenAI
import frontmatter
import re
import time   
import json

#SETUP
load_dotenv(override = True)

openai_key = os.getenv("OPENAI_API_KEY")

openai = OpenAI()

Docs_path = "security_doc"
Chunk_size = 500
Chunk_overlap = 50

encoder = tiktoken.get_encoding("cl100k_base")

#Read Single File
def read_md_file(file_path):
    with open(file_path, "r", encoding = "utf-8") as f:
        post = frontmatter.load(f)

        title = post.metadata.get("title", "")
        content = post.content

        return title, content

# count number of tokens 
def count_tokens(text):
    return len(encoder.encode(text))

def clean_heading(text):
    # remove HTML tags like <i class="..."></i>
    text = re.sub(r'<[^>]+>', '', text)
    # remove extra whitespace
    text = text.strip()
    return text

def parse_heading_chunks(content, title):
    lines = content.split("\n")
    
    chunks = []
    current_headings = {"h2": "", "h3": "", "h4": "", "h5": "", "h6": ""}
    current_lines = []

    for line in lines:
        if line.startswith("###### "):
            if current_lines:
                chunks.append({
                    "text": "\n".join(current_lines).strip(),
                    "headings": current_headings.copy()
                })
                current_lines = []
            current_headings["h6"] = clean_heading(line.replace("###### ", "").strip())

        elif line.startswith("##### "):
            if current_lines:
                chunks.append({
                    "text": "\n".join(current_lines).strip(),
                    "headings": current_headings.copy()
                })
                current_lines = []
            current_headings["h5"] = clean_heading(line.replace("##### ", "").strip())
            current_headings["h6"] = ""

        elif line.startswith("#### "):
            if current_lines:
                chunks.append({
                    "text": "\n".join(current_lines).strip(),
                    "headings": current_headings.copy()
                })
                current_lines = []
            current_headings["h4"] = clean_heading(line.replace("#### ", "").strip())
            current_headings["h5"] = ""
            current_headings["h6"] = ""

        elif line.startswith("### "):
            if current_lines:
                chunks.append({
                    "text": "\n".join(current_lines).strip(),
                    "headings": current_headings.copy()
                })
                current_lines = []
            current_headings["h3"] = clean_heading(line.replace("### ", "").strip())
            current_headings["h4"] = ""
            current_headings["h5"] = ""
            current_headings["h6"] = ""

        elif line.startswith("## "):
            if current_lines:
                chunks.append({
                    "text": "\n".join(current_lines).strip(),
                    "headings": current_headings.copy()
                })
                current_lines = []
            current_headings["h2"] = clean_heading(line.replace("## ", "").strip())
            current_headings["h3"] = ""
            current_headings["h4"] = ""
            current_headings["h5"] = ""
            current_headings["h6"] = ""

        else:
            current_lines.append(line)

    # catch last section
    if current_lines:
        chunks.append({
            "text": "\n".join(current_lines).strip(),
            "headings": current_headings.copy()
        })

    # remove empty chunks
    chunks = [c for c in chunks if c["text"].strip()]

    return chunks


def split_large_chunk(text, headings):
    # if chunk is within limit, return as is
    if count_tokens(text) <= Chunk_size:
        return [{"text": text, "headings": headings}]

    # if chunk contains HTML, return as is — don't split HTML blocks
    if "<table" in text or "<div" in text or "<ul" in text:
        return [{"text": text, "headings": headings}]

    # split by double newline (paragraphs)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    result = []
    current_paragraphs = []

    for paragraph in paragraphs:
        # check if adding this paragraph exceeds limit
        current_text = "\n\n".join(current_paragraphs)
        new_text = "\n\n".join(current_paragraphs + [paragraph])

        if count_tokens(new_text) > Chunk_size:
            # save current paragraphs as chunk
            if current_paragraphs:
                result.append({
                    "text": "\n\n".join(current_paragraphs).strip(),
                    "headings": headings
                })
                # overlap — carry last paragraph into next chunk
                # using last paragraph instead of raw tokens avoids mid-sentence cuts
                current_paragraphs = [current_paragraphs[-1], paragraph]
            else:
                # single paragraph too big, add it anyway
                result.append({
                    "text": paragraph,
                    "headings": headings
                })
                current_paragraphs = []
        else:
            current_paragraphs.append(paragraph)

    # catch the last piece
    if current_paragraphs:
        result.append({
            "text": "\n\n".join(current_paragraphs).strip(),
            "headings": headings
        })

    return result



def build_breadcrumb(title, headings):
    parts = [title]
    
    for level in ["h2", "h3", "h4", "h5", "h6"]:
        if headings[level]:
            parts.append(headings[level])
    
    return " > ".join(parts)

def generate_summary(text, breadcrumb):
    if count_tokens(text) < 30:
        return ""
    
    prompt = f"""You are helping build a RAG (Retrieval Augmented Generation) system for a security chatbot.

                Your job is to write a one-sentence summary of a policy section that will be stored as metadata.
                This summary will be used during retrieval — when a user asks a question, their question is
                compared against your summary to find the most relevant policy section.

                So your summary must:
                - Use plain everyday language a user would actually use when asking a question
                - Capture the core policy rule or procedure in the section
                - Be specific — mention the tool, process, or policy name if present
                - Avoid formal policy language like "this section outlines" or "this pertains to"

                Section location: {breadcrumb}

                Section content:
                {text}

                Write only the one sentence summary. Nothing else.
                """
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0
    )

    time.sleep(0.1)
    
    return response.choices[0].message.content.strip()


def process_file(file_path):
    # build URL from file path
    relative_path = Path(file_path).relative_to(Docs_path)
    
    # convert file path to URL
    url_path = str(relative_path).replace("_index.md", "").replace(".md", "/")
    url = f"https://handbook.gitlab.com/handbook/security/{url_path}"
    
    # read file
    title, content = read_md_file(file_path)
    
    # if no title in frontmatter, use filename as fallback
    if not title:
        title = Path(file_path).stem.replace("-", " ").title()
    
    # get heading based chunks
    heading_chunks = parse_heading_chunks(content, title)
    
    # split oversized chunks
    all_chunks = []
    for chunk in heading_chunks:
        split = split_large_chunk(chunk["text"], chunk["headings"])
        all_chunks.extend(split)
    
    # build final chunk objects with metadata
    final_chunks = []
    for i, chunk in enumerate(all_chunks):
        breadcrumb = build_breadcrumb(title, chunk["headings"])
        summary = generate_summary(chunk["text"], breadcrumb)
        
        final_chunks.append({
            # content
            "text": chunk["text"],
            
            # metadata
            "metadata": {
                "chunk_id": f"{relative_path}_{i}",
                "source_file": str(relative_path),
                "url": url,
                "page_title": title,
                "heading_h2": chunk["headings"]["h2"],
                "heading_h3": chunk["headings"]["h3"],
                "heading_h4": chunk["headings"]["h4"],
                "heading_h5": chunk["headings"]["h5"],
                "heading_h6": chunk["headings"]["h6"],
                "breadcrumb": breadcrumb,
                "section_summary": summary,
                "chunk_index": i,
                "token_count": count_tokens(chunk["text"])
            }
        })
    
    return final_chunks




# # cost estimator — no API calls made
# all_files = list(Path(Docs_path).rglob("*.md"))
# print(f"Total files: {len(all_files)}")

# total_chunks = 0
# total_tokens = 0

# for file_path in all_files:
#     try:
#         title, content = read_md_file(file_path)
#         if not title:
#             title = Path(file_path).stem.replace("-", " ").title()
#         heading_chunks = parse_heading_chunks(content, title)
#         all_chunks = []
#         for chunk in heading_chunks:
#             split = split_large_chunk(chunk["text"], chunk["headings"])
#             all_chunks.extend(split)
#         total_chunks += len(all_chunks)
#         for chunk in all_chunks:
#             total_tokens += count_tokens(chunk["text"])
#     except Exception as e:
#         print(f"ERROR in {file_path}: {e}")
#         continue

# print(f"Total chunks: {total_chunks}")
# print(f"Total tokens across all chunks: {total_tokens}")
# print(f"Estimated LLM calls for summaries: {total_chunks}")
# # gpt-4o-mini costs $0.15 per 1M input tokens
# estimated_cost = (total_tokens / 1_000_000) * 0.15
# print(f"Estimated cost: ${estimated_cost:.4f}")

def process_all_files(docs_path):
    all_files = list(Path(docs_path).rglob("*.md"))
    
    print(f"Found {len(all_files)} markdown files")
    
    all_chunks = []
    
    for i, file_path in enumerate(all_files):
        print(f"Processing {i+1}/{len(all_files)}: {file_path}")
        
        try:
            chunks = process_file(file_path)
            all_chunks.extend(chunks)
            print(f"  → {len(chunks)} chunks")
            
        except Exception as e:
            print(f"  → ERROR: {e}")
            continue
    
    print(f"\nTotal chunks across all files: {len(all_chunks)}")
    
    # save to JSON so we never need to regenerate
    output_path = "chunks.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to {output_path}")
    return all_chunks

if __name__ == "__main__":
    all_chunks = process_all_files(Docs_path)