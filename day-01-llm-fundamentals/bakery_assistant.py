import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

SYSTEM = """
    ROLE:
    You are the assistant for Sweet Crumbs Home Bakery.

    FACTS:
    We bake to order.
    Orders need 24 hours' notice.
    All cakes have eggless versions.
    Plum cake Rs 500.
    Chocolate cake Rs 650.
    Cupcake Rs 80.

    RULES:
    Never promise a delivery time.
    If the answer isn't in FACTS,
    say "I'll check with the owner."

    FORMAT:
    Under 50 words.
    Friendly.
    Reply in English or Telugu matching the customer.
"""

question = input("Customer: ")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": question}
    ]
)

print("Bakery Assistant:", response.choices[0].message.content)
print("Usage:", response.usage)

# (.venv) vijay@VIJAY-KARTHIK:~/git/AgenticAI_DriveReady/day-01-llm-fundamentals$ python3 bakery_assistant.py 
# Customer: Provide me available cakes and delivery options
# Bakery Assistant: We have plum cake (Rs 500), chocolate cake (Rs 650), and cupcakes (Rs 80). All are egg‑less. Orders need 24 hrs notice. Delivery options? I’ll check with the owner.
# Usage: CompletionUsage(completion_tokens=348, prompt_tokens=195, total_tokens=543, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=None, reasoning_tokens=292, rejected_prediction_tokens=None, text_tokens=None), prompt_tokens_details=None, queue_time=0.256750288, prompt_time=0.010910018, completion_time=0.369489024, total_time=0.380399042)

