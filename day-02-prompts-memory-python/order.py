import json
from typing import Any
from config import ORDER_EXTRACTION_SYSTEM
from experiment import get_messages_template,  get_response_with_messages

PRODUCTS = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80
}

PRODUCT_ALIASES = {
    "plum": "plum cake",
    "chocolate": "chocolate cake",
    "cupcakes": "cupcake"
}

def extract_order(user_prompt: str) -> dict[str, Any]:
    """
    Extract structured order information from the user's prompt.

    Args:
        user_prompt: User's order prompt.
    
    Returns:
        Dictionary containing the extracted order information.

    Raises:
        RunTimeError: If the LLM request fails
        ValueError: If the response is not valid JSON
    """
    messages = get_messages_template(system_prompt=ORDER_EXTRACTION_SYSTEM)
    response = get_response_with_messages(messages, user_prompt)

    if response.startswith("Error:"):
        raise RuntimeError(f"LLM request failed: {response}")

    try:
        data = json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response: {response}") from e

    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError(f"Invalid order structure: {data}")

    return data



def get_bill(data: dict[str, Any]) -> dict[str, Any]:
    """
    Calculate the bill for valid bakery products.

    Args:
        data: Extracted order containing an items list.

    Returns:
        Dictionary containing valid items, total amount and invalid items.
    """

    total = 0
    invalid_items = []
    valid_items = []

    for order_item in data["items"]:

        item = order_item["item"].lower().strip()
        item = PRODUCT_ALIASES.get(item, item)
        quantity = order_item["quantity"]

        if item not in PRODUCTS:
            invalid_items.append(order_item)
            continue

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            invalid_items.append(order_item)
            continue

        subtotal = PRODUCTS[item] * quantity

        valid_items.append({
            "item": item,
            "quantity": quantity,
            "subtotal": subtotal
        })

        total += subtotal

    return {
        "items": valid_items,
        "total": total,
        "invalid_items": invalid_items
    }