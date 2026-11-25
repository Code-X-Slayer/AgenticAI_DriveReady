# Day 2 — Experiments

This document records the experiments performed while developing the Sweet Crumbs Home Bakery chatbot.

## 1. Message Roles

**Objective:** Understand how different message roles influence LLM conversations.

Experimented with:
- `system` — defines assistant behaviour and instructions.
- `user` — contains customer input.
- `assistant` — contains previous assistant responses.

Created message lists manually and tested how conversation context influences subsequent responses.

**Observation:** The LLM can use previous messages to maintain conversational context.

## 2. Structured System Prompts

**Objective:** Control the assistant's behaviour using explicit instructions.

Experimented with:
- Role definition.
- Bakery information and product prices.
- Business rules.
- Response formatting.
- Language matching.
- Handling unknown information.

Compared prompts with and without explicit formatting instructions.

**Observation:** Clear instructions and relevant business context help produce more consistent responses.

## 3. Zero-Shot and Few-Shot Classification

**Objective:** Classify customer messages into three categories:

- `order`
- `question`
- `complaint`

Test messages:

| Customer message | Expected category |
|---|---|
| I want three cupcakes. | order |
| What is the price of chocolate cake? | question |
| The cake arrived damaged. | complaint |
| Please book one plum cake. | order |
| Do you make eggless cupcakes? | question |

Experimented with:
- Zero-shot classification using category definitions.
- Few-shot classification using example user-assistant pairs.

**Observation:** Both approaches classified the tested messages correctly. Few-shot prompting provides concrete examples of the expected output.

## 4. Structured JSON Extraction

**Objective:** Extract order information from natural-language messages.

Expected structure:

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

Test cases:

| Input | Expected extraction |
|---|---|
| I need 2 plum cakes and 3 cupcakes. | Two products with quantities |
| I need 2 vanilla cakes. | Vanilla cake, quantity 2 |
| I need 2 plum cakes and 1 vanilla cake. | Two products |
| I need cupcakes. | Cupcake, quantity null |

**Observation:**
- The LLM can extract multiple products.
- Missing quantities can be represented using `null`.
- Unsupported products should still be extracted rather than silently discarded.
- JSON parsing converts the response into a Python dictionary.

## 5. Python-Based Billing

**Objective:** Calculate order totals without relying on the LLM for arithmetic or pricing.

Product dictionary:

```python
PRODUCTS = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80
}
```

Tested:
- Valid products.
- Unsupported products.
- Missing quantities.
- Multiple products in one order.
- Invalid quantities.

Example:

```text
2 plum cakes = ₹1000
3 cupcakes = ₹240

Total = ₹1240
```

**Observation:** Product validation and billing should be handled deterministically in Python. The LLM should extract customer intent and order details, not determine authoritative prices.

## 6. Conversation History

**Objective:** Understand how previous messages can be retained and reused.

Tested a conversation where the customer:
1. Introduced themselves as Vijay.
2. Asked for two plum cakes.
3. Later asked for their name and previous order.

**Observation:** Passing the existing message list to subsequent LLM calls allows the assistant to refer to earlier messages within the conversation.

## 7. Dictionaries and JSON Operations

Practised:
- Creating and accessing dictionaries.
- Iterating through lists of dictionaries.
- Reading nested values.
- Converting JSON strings into Python dictionaries using `json.loads()`.
- Validating extracted fields.
- Building structured billing results.

## 8. Functions, Type Hints and Docstrings

Organised repeated operations into reusable functions.

Examples:
- `get_messages_template()`
- `get_response_with_messages()`
- `classify_message()`
- `extract_order()`
- `get_bill()`

Added type hints and docstrings to clarify function inputs, outputs, and responsibilities.

## 9. Decorators

Implemented a timer decorator using:
- `functools.wraps`
- `time.perf_counter()`
- `*args` and `**kwargs`

Applied it to the LLM response function to measure execution time.

**Observation:** Decorators allow additional behaviour to be applied to functions without modifying their core implementation.

## 10. Exception Handling

Tested API failure scenarios, including:
- Invalid API key.
- Rate-limit errors.
- Connection errors.
- API status errors.
- Unexpected exceptions.
- Invalid JSON responses.

Used specific exception handling and error messages to prevent common API failures from being mistaken for successful results.

## 11. Final Chatbot Integration

Integrated the modules into a command-line application.

Basic flow:

```text
Customer Input
      |
      v
Message Classifier
      |
      +---- order
      |       |
      |       v
      |   JSON Extraction
      |       |
      |       v
      |   Python Billing
      |
      +---- question
      |       |
      |       v
      |   Customer Assistant
      |
      +---- complaint
              |
              v
          Customer Assistant
```

Tested:
- Greetings.
- Product and price questions.
- Order extraction and billing.
- Unsupported products.
- Missing quantities.
- Delivery-related questions.
- Exit handling.

**Final observation:** The integrated prototype successfully demonstrates intent classification, order extraction, deterministic billing, and basic conversational responses. More work is needed for persistent order context, confirmation, and specialised complaint handling.

---

## Overall Learning

The most important takeaway from these experiments:

**LLMs handle natural language and intent. Python handles deterministic business logic, validation, and calculations.**

Combining both creates a more reliable application than relying on the LLM for everything.