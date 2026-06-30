import gradio as gr
from query import answer

def chat(user_message, history):
    result = answer(user_message)

    return result["answer"]


demo = gr.ChatInterface(
    fn=chat,
    title="Security Handbook Assistant",
    description="Ask questions about GitLab's security policies and handbook. Powered by RAG + Knowledge Graph.",
    examples=[
        "What is the VPN policy?",
        "What happens if I find a vulnerability?",
        "How do I engage the security team on-call?",
        "What are the password guidelines?",
        "What is the vulnerability remediation SLA?",
    ],

)

if __name__ == "__main__":
    demo.launch(share=True)
