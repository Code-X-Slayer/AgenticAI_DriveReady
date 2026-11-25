from experiment import get_response_with_messages
from config import CLASSIFICATION_SYSTEM


if __name__ == "__main__":
    queries = [
        "I want three cupcakes.",
        "What is the price of chocolate cake?",
        "The cake arrived damaged.",
        "Please book one plum cake.",
        "Do you make eggless cupcakes?"
    ]
    
    # zero shot
    messages = [
        {"role": "system", "content": CLASSIFICATION_SYSTEM},
    ]

    print("Zero shot classification:")

    for query in queries:
        print(f"Query: {query}")
        print(f"Category: {get_response_with_messages(messages[:], query)}")
        print()


    # few shot
    messages = [
        {"role": "system", "content": CLASSIFICATION_SYSTEM},

        {"role": "user", "content": "I need two plum cakes."},
        {"role": "assistant", "content": "order"},

        {"role": "user", "content": "Do you have eggless cakes?"},
        {"role": "assistant", "content": "question"},

        {"role": "user", "content": "My cake was damaged."},
        {"role": "assistant", "content": "complaint"},
    ]

    print("Few shot classification:")

    for query in queries:
        print(f"Query: {query}")
        print(f"Category: {get_response_with_messages(messages[:], query)}")
        print()

    # Zero shot classification:
    # Query: I want three cupcakes.
    # Category: order

    # Query: What is the price of chocolate cake?
    # Category: question

    # Query: The cake arrived damaged.
    # Category: complaint

    # Query: Please book one plum cake.
    # Category: order

    # Query: Do you make eggless cupcakes?
    # Category: question

    # Few shot classification:
    # Query: I want three cupcakes.
    # Category: order

    # Query: What is the price of chocolate cake?
    # Category: question

    # Query: The cake arrived damaged.
    # Category: complaint

    # Query: Please book one plum cake.
    # Category: order

    # Query: Do you make eggless cupcakes?
    # Category: question

def classify_message(user_prompt: str) -> str:
    """
    Classify a user message into one of the categories: order, question, complaint.

    Args:
        user_prompt: The user's message to classify.

    Returns:
        The assistant's response as a string.
    """
    messages = [
        {"role": "system", "content": CLASSIFICATION_SYSTEM},

        {"role": "user", "content": "I need two plum cakes."},
        {"role": "assistant", "content": "order"},

        {"role": "user", "content": "Do you have eggless cakes?"},
        {"role": "assistant", "content": "question"},

        {"role": "user", "content": "My cake was damaged."},
        {"role": "assistant", "content": "complaint"},
    ]

    category = get_response_with_messages(messages, user_prompt).strip().lower()

    if category not in ["order", "question", "complaint"]:
        raise ValueError(f"Invalid category returned: {category}")

    return category

