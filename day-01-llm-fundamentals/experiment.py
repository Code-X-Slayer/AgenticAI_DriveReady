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

# =====================================================================
# exp1 : comparing temperature 0.2 and 1.2
# =====================================================================

# response1 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=0.2,
#     messages = [
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "Provide me available cakes and delivery options"}
#     ]
# )
# print("Bakery Assistant (temperature=0.2):", response1.choices[0].message.content)

# response2 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=1.2,
#     messages = [
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "Provide me available cakes and delivery options"}
#     ]
# )
# print("Bakery Assistant (temperature=1.2):", response2.choices[0].message.content)

# (.venv) vijay@VIJAY-KARTHIK:~/git/AgenticAI_DriveReady/day-01-llm-fundamentals$ python3 experiment.py 
# Bakery Assistant (temperature=0.2): We offer plum cake (Rs 500), chocolate cake (Rs 650), and cupcakes (Rs 80). All have eggless versions. Orders need 24‑hour notice. I’ll check with the owner for delivery options.
# Bakery Assistant (temperature=1.2): Here’s what we have:

# - Plum cake: Rs 500  
# - Chocolate cake: Rs 650  
# - Cupcake: Rs 80

# All are egg‑free.  

# I’ll check with the owner about delivery options and get back to you!


# =====================================================================
# exp2: test hallunications without business facts
# =====================================================================

# response1 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=0.2,
#     messages = [
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "What is the price of a vanilla cake?"}
#     ]
# )
# print("Bakery Assistant (temperature=0.2):", response1.choices[0].message.content)  

# response2 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=1.2,
#     messages = [
#         {"role": "system", "content": "You are the assistant for Sweet Crumbs Home Bakery."},
#         {"role": "user", "content": "What is the price of a vanilla cake?"}
#     ]
# )
# print("Bakery Assistant (temperature=1.2):", response2.choices[0].message.content)
# (.venv) vijay@VIJAY-KARTHIK:~/git/AgenticAI_DriveReady/day-01-llm-fundamentals$ python3 experiment.py
# Bakery Assistant (temperature=0.2): I’ll check with the owner.
# Bakery Assistant (temperature=1.2): **Sweet Crumbs Home Bakery – Vanilla Cake**

# The price varies a bit depending on the size and any special touches you want, but here’s a quick rundown of our standard rates:

# | Size | Price |
# |------|-------|
# | 8‑inch (approx. 16 servings) | **$30.00** |
# | 10‑inch (approx. 30–35 servings) | **$45.00** |
# | 12‑inch (approx. 50–60 servings) | **$60.00** |

# *Custom décor or special flavor notes can add $10–$20 on top of these base prices.*

# If you need a different size, a special design, or want to place an order, just let us know and we’ll give you a personalized quote. Happy baking! 🍰



# =====================================================================
# exp3: compare seperate api calls with conversation history
# =====================================================================

# response1 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=0.2,    
#     messages = [
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "Provide me available cakes and delivery options"}
#     ]
# )
# print("Bakery Assistant (turn 1):", response1.choices[0].message.content)

# response2 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=0.2,
#     messages = [
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "Provide me available cakes and delivery options"},
#         {"role": "assistant", "content": response1.choices[0].message.content
#         },
#         {"role": "user", "content": "What is the price of a plum cake and cupcake ?"}
#     ]
# )
# print("Bakery Assistant (turn 2):", response2.choices[0].message.content)

# (.venv) vijay@VIJAY-KARTHIK:~/git/AgenticAI_DriveReady/day-01-llm-fundamentals$ python3 experiment.py
# Bakery Assistant (turn 1): We offer plum cake (Rs 500), chocolate cake (Rs 650), and cupcakes (Rs 80). All are egg‑less. For delivery details, I’ll check with the owner.
# Bakery Assistant (turn 2): Plum cake is Rs 500, and a cupcake is Rs 80.

# =====================================================================
# exp4: compare english and telugu token usage
# =====================================================================

# response1 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=0.2,
#     messages = [
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "Provide me available cakes and delivery options in english"}
#     ]
# )
# print("Bakery Assistant (English):", response1.choices[0].message.content)
# print("English token usage:", response1.usage.completion_tokens)

# response2 = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=0.2,
#     messages = [
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "Provide me available cakes and delivery options in telugu"}
#     ]
# )
# print("Bakery Assistant (Telugu):", response2.choices[0].message.content)
# print("Telugu token usage:", response2.usage.completion_tokens)

# (.venv) vijay@VIJAY-KARTHIK:~/git/AgenticAI_DriveReady/day-01-llm-fundamentals$ python3 experiment.py
# Bakery Assistant (English): We offer Plum cake (Rs 500), Chocolate cake (Rs 650), and Cupcake (Rs 80), all egg‑less. All are made to order with 24‑hour notice. Delivery details? I'll check with the owner.
# English token usage: 338
# Bakery Assistant (Telugu): మా అందుబాటులో ఉన్న కేకులు: ప్లమ్ కేక్ (₹500), చాక్లెట్ కేక్ (₹650), కప్‌కేక్ (₹80). అన్ని ఎగ్‌లెస్ వెర్షన్‌లో అందుబాటులో ఉన్నాయి. ఆర్డర్‌కు 24 గంటల ముందస్తు నోటీసు అవసరం. డెలివరీ ఎంపికల గురించి నేను యజమానికి చెక్ చేస్తాను.
# Telugu token usage: 562