import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from retriever import search

load_dotenv(override = True)
client = OpenAI()

class SubQuestions(BaseModel):
    questions: list[str]

class AnsweredQuestion(BaseModel):
    question : str
    answer : str

class AnsweredQuestions(BaseModel):
    answers : list[AnsweredQuestion]

def generate_prompt(query):

    return f"""
        "You are a helpful assistant that prepares queries that will be sent to a search component.\n"
        "Sometimes, these queries are very complex.\n"
        "Your job is to simplify complex queries into multiple queries that can be answered "
        "in isolation to each other.\n\n"
        "If the query is simple, then keep it as it is.\n\n"
        "Examples\n"
        "1. Query: Did Microsoft or Google make more money last year?\n"
        "   Decomposed Questions: [\"How much profit did Microsoft make last year?\", "
        "\"How much profit did Google make last year?\"]\n"
        "2. Query: What is the capital of France?\n"
        "   Decomposed Questions: [\"What is the capital of France?\"]\n\n"
        f"Query: {query}\n"
        "Decomposed Questions:"
    """

def decompose_query(query):
    response = client.chat.completions.parse(
        model = "gpt-4o-mini",
        messages = [{
            "role" : "user",
            "content" : generate_prompt(query)
        }],
        response_format=SubQuestions
    )

    return response.choices[0].message.parsed.questions

def get_question_context_pairs(subquestions, top_k = 5):
    pairs = []
    for question in subquestions:
        results = search(question, top_k)
        pairs.append({
            "question" : question,
            "context" : results
        })
    return pairs

def generate_answer_prompt(pairs):
    sections = ""
    for pair in pairs:
        context_text = "\n---\n".join(r["text"] for r in pair["context"])
        sections += f"\nQuestion: {pair['question']}\nContext:\n{context_text}\n"

    return f"""You are a helpful assistant answering questions using only the provided context.
        For each question, answer it using only its matching context, and mention which
        section the answer came from.
        If the context doesn't contain the answer to a question, say so for that question
        instead of guessing.

        Examples

        Question: What is the remediation SLA for a critical severity finding?
        Context: Observation remediation SLA's are determined by the risk rating of the
        individual observation. | Risk Rating: Critical | Remediation SLA: 3 months |
        Answer: Critical findings have a 3-month remediation SLA, per the Observation
        Management Procedure's remediation SLA table.

        Question: Who approves SLA exceptions for FedRAMP findings?
        Context: Observation remediation SLA's are determined by the risk rating of the
        individual observation. | Risk Rating: Critical | Remediation SLA: 3 months |
        Answer: I could not find who approves SLA exceptions for FedRAMP findings in
        the provided context.

        {sections}
        """
  
def answer_sub_questions(subquestions):
    pairs = get_question_context_pairs(subquestions)
    prompt = generate_answer_prompt(pairs)

    response = client.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format=AnsweredQuestions,
    )
    return response.choices[0].message.parsed.answers

def generate_synthesis_prompt(original_query, answers):
    qa_text = ""
    for a in answers:
        qa_text += f"\nSub-question: {a.question}\nAnswer: {a.answer}\n"

    return f"""You have broken a user's question down into simpler sub-questions,
    and answered each one individually using retrieved policy context.

    Original question: {original_query}

    Sub-questions and their answers:
    {qa_text}

    Using the answers above, write one clear, direct answer to the original question.
    Combine the sub-answers naturally instead of just listing them separately.
    If any sub-answer indicates the information could not be found, mention that
    limitation in your final answer instead of ignoring it.
    """

def synthesize_answer(original_query, answers):
    prompt = generate_synthesis_prompt(original_query, answers)

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [{"role":"user", "content":prompt},
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()
   
if __name__ == "__main__":
   query = "I'm designing an internal audit. For each of the following, tell me who has to approve it and what document governs it: (a) granting a contractor access to an internal Google Workspace group, (b) requesting a permanent exception to a vulnerability SLA, (c) adjusting the severity label on an already-triaged security incident."
   sub_questions = decompose_query(query)
   answers = answer_sub_questions(sub_questions)
   final_answer = synthesize_answer(query, answers)
   print("\nFinal Answer:")
   print(final_answer)
