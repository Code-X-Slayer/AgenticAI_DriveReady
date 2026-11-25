# Day 2 — Prompt Engineering, Conversation Memory & Python LLM Integration

A command-line chatbot for **Sweet Crumbs Home Bakery**, built using Python and the Groq API.

This project explores how to build an LLM-powered application using structured prompts, message roles, few-shot classification, JSON extraction, conversation history, decorators, exception handling, and modular Python code.

## Features

- **Role-based conversations:** Uses system, user, and assistant messages.
- **Structured system prompts:** Defines the bakery assistant's role, product information, pricing, and response rules.
- **Zero-shot and few-shot classification:** Classifies customer messages into orders, questions, and complaints.
- **Structured JSON extraction:** Extracts product names and quantities from natural-language orders.
- **Python-based billing:** Validates products and quantities and calculates totals using predefined prices.
- **Conversation history:** Maintains message history for customer-facing conversations.
- **Decorators:** Measures LLM function execution time.
- **Exception handling:** Handles common API errors and invalid JSON responses.
- **Modular architecture:** Separates configuration, LLM communication, classification, and order processing.

## Tech Stack

- Python
- Groq API
- OpenAI Python SDK
- JSON
- python-dotenv

## Project Structure

```text
day-02-prompts-memory-python/
│
├── config.py
├── experiment.py
├── message_roles.py
├── prompt_builder.py
├── classifier_zero_few_shot.py
├── chat_history.py
├── json_task.py
├── order.py
├── main.py
│
├── experiments.md
├── notes.md
├── README.md
│
└── .env
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd day-02-prompts-memory-python
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

### 4. Configure the API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file or expose your API key.

### 5. Run the chatbot

```bash
python3 main.py
```

## Bakery Information

The chatbot uses the following sample product catalogue:

| Product | Price |
|---|---:|
| Plum Cake | ₹500 |
| Chocolate Cake | ₹650 |
| Cupcake | ₹80 |

Additional business rules:
- Orders require 24 hours' notice.
- Eggless versions are available.
- Unknown information should be referred to the bakery owner.
- The chatbot must not promise delivery times.

## Example Interaction

```text
user: hello

assistant: Hello! How can I help you with your sweet order?

user: What items do you provide and what are their prices?

assistant:
Plum cake - ₹500
Chocolate cake - ₹650
Cupcake - ₹80

user: I would like to order 3 plum cakes and 2 chocolate cakes.

assistant:
Order summary
Plum cake - 3 - ₹1500
Chocolate cake - 2 - ₹1300
Total: ₹2800
```

## Learning Outcomes

By completing this project, I practised:

1. LLM message roles and conversation structure.
2. Writing structured system prompts.
3. Zero-shot and few-shot prompting.
4. Extracting structured data from LLM responses.
5. Parsing and validating JSON.
6. Python dictionaries and data processing.
7. Functions, type hints, and docstrings.
8. Decorators and execution-time measurement.
9. Exception handling for API requests.
10. Integrating multiple Python modules into a working chatbot.

## Current Limitations

This is a learning prototype, not a production-ready ordering system.

- Conversation history is maintained in memory only.
- Order state is not yet persisted across conversations.
- Order confirmation and actual order placement are not implemented.
- Product aliases and normalization need further improvement.
- Complaint handling currently uses the general customer-facing assistant.
- Delivery scheduling and payment processing are not implemented.

## Next Improvements

- Add structured conversation state.
- Make follow-up questions aware of previous orders.
- Improve product normalization and validation.
- Separate complaint handling from general questions.
- Add automated tests.
- Improve response formatting and error recovery.

---

**Project:** Agentic AI Drive Ready — Day 2  
**Application:** Sweet Crumbs Home Bakery Chatbot  
**Focus:** Prompt Engineering, Memory, JSON Extraction and Python Integration