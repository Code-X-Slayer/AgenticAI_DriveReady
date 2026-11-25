# Day 2 — Learning Notes

## 1. Message Roles

LLM conversations are represented as a sequence of messages.

| Role | Purpose |
|---|---|
| system | Defines assistant behaviour |
| user | Contains user input |
| assistant | Contains assistant responses |

The conversation history is passed to the model as a list of dictionaries.

## 2. System Prompts

A good system prompt should clearly define:

- Role: Who is the assistant?
- Context: What information does it know?
- Rules: What should it and shouldn't it do?
- Format: How should it respond?

Specific instructions generally make behaviour easier to control.

## 3. Zero-Shot vs Few-Shot Prompting

**Zero-shot:** Ask the model to perform a task without providing examples.

**Few-shot:** Provide example inputs and expected outputs before the actual query.

Few-shot prompting helps demonstrate the desired response pattern.

## 4. JSON Extraction

LLMs can convert natural-language requests into structured JSON.

Example:

```json
{
    "category": "order",
    "items": [
        {
            "item": "plum cake",
            "quantity": 2
        }
    ]
}
```

Important:

- JSON is a string when received from an API.
- `json.loads()` converts a JSON string into Python objects.
- `json.dumps()` converts Python objects into JSON strings.
- `null` in JSON becomes `None` in Python.
- Invalid JSON should be handled using `json.JSONDecodeError`.

## 5. Dictionaries

Dictionaries store key-value pairs.

```python
product = {
    "item": "plum cake",
    "quantity": 2,
    "price": 500
}
```

Access values:

```python
product["item"]
product["quantity"]
```

Iterate through a list of dictionaries:

```python
for item in order["items"]:
    print(item["item"], item["quantity"])
```

## 6. Function Design

Functions should have clear responsibilities.

Example:

```python
def get_bill(data: dict) -> dict:
    ...
```

- Type hints describe expected input and output types.
- Docstrings explain a function's purpose, parameters, and return value.
- Smaller functions make code easier to test and maintain.

## 7. Decorators

A decorator wraps an existing function to add behaviour.

Basic structure:

```python
from functools import wraps

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Additional behaviour
        result = func(*args, **kwargs)
        return result

    return wrapper
```

`*args` accepts positional arguments.

`**kwargs` accepts keyword arguments.

`@wraps(func)` preserves the original function's metadata.

## 8. Exception Handling

Use `try` and `except` to handle errors without unexpectedly terminating an application.

Examples:

```python
try:
    data = json.loads(response)

except json.JSONDecodeError:
    print("Invalid JSON")
```

Common API exceptions tested:
- `AuthenticationError`
- `RateLimitError`
- `APIConnectionError`
- `APIStatusError`

Prefer handling specific exceptions before using a general `Exception` handler.

## 9. LLM Integration

The basic interaction pattern:

```python
messages = get_messages_template()

response = get_response_with_messages(
    messages,
    user_prompt
)
```

Important distinction:

- `get_messages_template()` returns a message list.
- `get_response_with_messages()` returns a response string.
- `json.loads()` returns parsed Python data.

Never confuse a message list with an LLM response string.

## 10. Application Architecture

Keep different responsibilities in separate modules.

| Module | Responsibility |
|---|---|
| config.py | Prompts and configuration |
| experiment.py | API client and message handling |
| classifier_zero_few_shot.py | Intent classification |
| order.py | Order extraction and billing |
| main.py | Application flow and routing |

## 11. Important Design Lessons

1. Don't use an LLM for deterministic calculations.
2. Keep product prices in Python rather than asking the model to calculate them.
3. Validate LLM-generated data before using it.
4. Preserve the original customer input.
5. Use separate prompts for different tasks.
6. Keep conversation history separate from task-specific extraction.
7. Handle API failures and invalid responses.
8. Don't confuse an order summary with an order confirmation.
9. A working prototype is not necessarily production-ready.

## 12. Improvements to Explore Later

- Structured conversation state and order memory.
- Product aliases and canonical product-name mapping.
- Better handling of incomplete orders.
- Separate complaint-handling prompts.
- Order confirmation workflow.
- Automated unit and integration tests.
- Persistent storage using a database.

---

## Day 2 Takeaway

A useful LLM application is not just a prompt connected to an API.

It requires structured inputs, controlled context, validation, deterministic business logic, reusable functions, error handling, and a clear application architecture.