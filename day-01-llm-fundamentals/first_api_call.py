import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain What an LLM is in simple words and how its useful in agentic ai."
        }
    ]
)

print(response.choices[0].message.content)
print(response.usage)

# (.venv) vijay@VIJAY-KARTHIK:~/git/AgenticAI_DriveReady/day-01-llm-fundamentals$ python3 first_api_call.py 
# ### 1. What is an LLM? (In plain English)

# | **What** | **Why it matters** | **How it works (very briefly)** |
# |----------|--------------------|---------------------------------|
# | **LLM = Large Language Model** | It’s a computer program that *understands* and *generates* human‑like text. | It was trained on billions of words from books, websites, news, etc. During training it learned patterns, grammar, facts, and even some reasoning tricks. |

# **Think of it like this:**  
# - Imagine a gigantic, super‑fast “brain” that has read almost every book and article you can think of.  
# - When you ask it a question or give it a prompt, it uses all that reading to produce a coherent answer, story, or instruction.

# ### 2. How LLMs are useful in *agentic AI*

# **Agentic AI** = AI that can *act* in a world, make decisions, plan, and pursue goals—kind of like a digital “agent” that can do things on its own.

# | **Role of an LLM in an agent** | **Why it helps** | **Example** |
# |--------------------------------|------------------|-------------|
# | **Natural‑language interface** | Lets humans talk to the agent in plain English. | A customer‑service bot that understands and replies to user queries. |
# | **Planning & reasoning** | The LLM can generate possible next steps, evaluate options, and even explain its reasoning. | A home‑automation agent that decides whether to turn on lights, lock doors, or adjust the thermostat based on a spoken request. |
# | **Knowledge base** | It carries a huge amount of factual information that the agent can draw on instantly. | A medical triage assistant that can recall symptoms and suggest possible conditions. |
# | **Policy guidance** | In reinforcement‑learning setups, the LLM can act as a *policy network*—suggesting actions that maximize a goal. | A game‑playing AI that uses the LLM to decide the next move in a strategy game. |
# | **Self‑reflection & debugging** | The agent can ask the LLM to explain why it made a decision or to check for mistakes. | A robotic assistant that logs its actions and can be asked to explain why it chose a particular path. |

# ### 3. Putting it together: A simple “agent” example

# 1. **Goal** – “Help me plan a trip to Paris.”  
# 2. **LLM** receives the user’s request, understands the goal, and asks clarifying questions (“When are you traveling?”).  
# 3. **LLM** fetches relevant facts (e.g., best travel dates, visa requirements) and generates a plan (flight options, hotel suggestions, itinerary).  
# 4. **Agent** sends the plan back to the user, can book tickets, and can later answer follow‑up questions (“What’s the weather like on the 15th?”).  

# In this loop, the LLM is the *brain* that interprets language, pulls in knowledge, and decides what to do next—exactly what an agent needs to be “agentic.”

# ### 4. Quick Takeaway

# - **LLM** = a huge, text‑trained model that can read, write, and reason in natural language.  
# - **Agentic AI** = an AI that can act autonomously.  
# - **Why LLMs matter for agents**: they give the agent a powerful language interface, built‑in knowledge, and the ability to plan and explain—making the agent smarter, more flexible, and easier for humans to interact with.
# CompletionUsage(completion_tokens=962, prompt_tokens=98, total_tokens=1060, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=None, reasoning_tokens=194, rejected_prediction_tokens=None, text_tokens=None), prompt_tokens_details=None, queue_time=0.368074039, prompt_time=0.005407488, completion_time=0.976277139, total_time=0.981684627)

