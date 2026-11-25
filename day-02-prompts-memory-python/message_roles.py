from config import SYSTEM
from experiment import get_response_with_messages

messages = [
    {
        "role": "system",
        "content": SYSTEM
    },
    {
        "role": "user",
        "content": "My name is Vijay."
    },
    {
        "role": "assistant",
        "content": "Nice to meet you, Vijay!"
    }
]

print(get_response_with_messages(messages, "What is my name?"))
# You mentioned that your name is Vijay.

