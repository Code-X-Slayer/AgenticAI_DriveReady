# Day 01 - LLM Fundamentals

## Topics Covered
- What is an LLM?
- LLMs in Agentic AI
- Tokens and Temperature
- Context Window and Memory
- Hallucinations
- First LLM API Call

## Files
- `first_api_call.py` - First API call using Groq.
- `bakery_assistant.py` - Simple bakery AI assistant.
- `experiment.py` - Experiments with temperature, hallucinations, memory and token usage.
- `notes.md` - Concepts learned.
- `experiments.md` - Experiment results and observations.

## Tech Stack
- Python
- Groq API
- OpenAI Python SDK
- python-dotenv

## Setup

```bash
pip install openai python-dotenv
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
python3 first_api_call.py
python3 bakery_assistant.py
python3 experiment.py
```

## What I Built
1. Connected Python with an LLM using Groq.
2. Created a simple bakery assistant using system prompts.
3. Explored temperature, hallucinations, conversation history and token usage.

## Status
Day 01 completed.