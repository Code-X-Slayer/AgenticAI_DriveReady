import os
from typing import Any
from dotenv import load_dotenv
from openai import APIConnectionError, APIStatusError, AuthenticationError, OpenAI, RateLimitError
from config import SYSTEM
import time
from functools import wraps

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def timer(func):
    """
    Decorator to measure the execution time of a function.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function that measures execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return res
    return wrapper


def get_messages_template(system_prompt: str = SYSTEM) -> list[dict[str, str]]:
    """
    Create the initial conversation message list.

    Args:
        system_prompt: Instructions defining the assistant's behavior.

    Returns:
        A list containing the system message.
    """
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]
    return messages

@timer
def get_response_with_messages(
    messages: list[dict[str, str]],
    user_prompt: str
) -> str:
    """
    Send a user message to the LLM and maintain conversation history.

    Args:
        messages: Existing conversation history.
        user_prompt: The latest user message.

    Returns:
        The assistant's response as a string.
    """
    messages.append({
        "role": "user",
        "content": user_prompt
    })

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )

        assistant_response = response.choices[0].message.content or ""

        messages.append({
            "role": "assistant",
            "content": assistant_response
        })

        return assistant_response

    except AuthenticationError:
        print("LLM Error: Invalid API key. Please check your GROQ_API_KEY.")
        return "Error: Invalid API key."

    except RateLimitError:
        print("LLM Error: Rate limit exceeded. Please try again later.")
        return "Error: Rate limit exceeded."

    except APIConnectionError:
        print("LLM Error: Connection error. Please check your network connection.")
        return "Error: Connection error."

    except APIStatusError:
        print("LLM Error: API status error. Please try again later.")
        return "Error: API status error."

    except Exception as e:
        print(f"LLM Error: {e}")
        return "Error: Unable to get a response from the LLM."
