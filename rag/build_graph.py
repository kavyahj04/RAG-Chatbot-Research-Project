import json
import re
import pickle
from pathlib import Path
import networkx as nx
from collections import defaultdict

# load chunks
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks")

# create directed graph
G = nx.DiGraph()

# add every chunk as a node
for chunk in chunks:
    G.add_node(
        chunk["metadata"]["chunk_id"],
        text=chunk["text"],
        breadcrumb=chunk["metadata"]["breadcrumb"],
        url=chunk["metadata"]["url"],
        source_file=chunk["metadata"]["source_file"],
        page_title=chunk["metadata"]["page_title"],
        heading_h2=chunk["metadata"]["heading_h2"],
        heading_h3=chunk["metadata"]["heading_h3"],
        heading_h4=chunk["metadata"]["heading_h4"],
        heading_h5=chunk["metadata"]["heading_h5"],   
        heading_h6=chunk["metadata"]["heading_h6"],   
        chunk_index=chunk["metadata"]["chunk_index"]
    )

print(f"Nodes added: {G.number_of_nodes()}")


# build lookup: source_file → list of chunks in order
from collections import defaultdict

file_chunks = defaultdict(list)
for chunk in chunks:
    file_chunks[chunk["metadata"]["source_file"]].append(chunk)

# sort each file's chunks by chunk_index
for source_file in file_chunks:
    file_chunks[source_file].sort(key=lambda x: x["metadata"]["chunk_index"])

# add heading hierarchy edges
edge_count = 0

for source_file, file_chunk_list in file_chunks.items():
    for i, chunk in enumerate(file_chunk_list):
        current_breadcrumb = chunk["metadata"]["breadcrumb"]
        current_id = chunk["metadata"]["chunk_id"]
        
        # look ahead — find the next chunk in the same file
        if i + 1 < len(file_chunk_list):
            next_chunk = file_chunk_list[i + 1]
            next_id = next_chunk["metadata"]["chunk_id"]
            
            # connect sequential chunks within same file
            G.add_edge(current_id, next_id, relationship="next_section")
            G.add_edge(next_id, current_id, relationship="prev_section")
            edge_count += 1

print(f"Heading hierarchy edges added: {edge_count}")

# build lookup: url → chunk_id for finding targets
url_to_chunks = defaultdict(list)
for chunk in chunks:
    url_to_chunks[chunk["metadata"]["url"]].append(chunk["metadata"]["chunk_id"])

# add folder hierarchy edges
folder_edge_count = 0

for chunk in chunks:
    source_file = chunk["metadata"]["source_file"]
    current_id = chunk["metadata"]["chunk_id"]
    
    # get parent path
    # e.g. "vulnerability-management/sla-exceptions.md"
    # parent is "vulnerability-management/_index.md"
    parts = Path(source_file).parts
    
    if len(parts) > 1:
        # build parent path
        parent_path = str(Path(*parts[:-1]) / "_index.md")
        
        # find parent chunks
        parent_chunks = [
            c for c in chunks 
            if c["metadata"]["source_file"] == parent_path
        ]
        
        if parent_chunks:
            # connect to first chunk of parent page
            parent_id = parent_chunks[0]["metadata"]["chunk_id"]
            
            if not G.has_edge(parent_id, current_id):
                G.add_edge(parent_id, current_id, relationship="parent_of")
                G.add_edge(current_id, parent_id, relationship="child_of")
                folder_edge_count += 1

print(f"Folder hierarchy edges added: {folder_edge_count}")

# add markdown link edges
link_edge_count = 0

# build lookup: url path → chunk_ids
path_to_chunks = defaultdict(list)
for chunk in chunks:
    # extract path from full url
    # https://handbook.gitlab.com/handbook/security/vulnerability-management/
    # → /handbook/security/vulnerability-management/
    url = chunk["metadata"]["url"]
    path = url.replace("https://handbook.gitlab.com", "")
    path_to_chunks[path].append(chunk["metadata"]["chunk_id"])

for chunk in chunks:
    current_id = chunk["metadata"]["chunk_id"]
    text = chunk["text"]
    
    # extract all markdown links from chunk text
    links = re.findall(r'\[.*?\]\((.*?)\)', text)
    
    for link in links:
        # only process internal handbook links
        if not link.startswith("/handbook/security"):
            continue
        
        # normalize link — remove anchors like #section-name
        link = link.split("#")[0]
        
        if not link.endswith("/"):
            link += "/"
        
        # find chunks at this url path
        target_chunks = path_to_chunks.get(link, [])
        
        for target_id in target_chunks:
            if target_id != current_id and not G.has_edge(current_id, target_id):
                G.add_edge(current_id, target_id, relationship="references")
                link_edge_count += 1

print(f"Markdown link edges added: {link_edge_count}")

# save graph to disk
output_path = "graph.pkl"

with open(output_path, "wb") as f:
    pickle.dump(G, f)

print(f"\nGraph saved to {output_path}")
print(f"Total nodes: {G.number_of_nodes()}")
print(f"Total edges: {G.number_of_edges()}")