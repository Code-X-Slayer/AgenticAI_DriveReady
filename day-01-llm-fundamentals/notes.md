# Day 01 - Notes

## 1. LLM (Large Language Model)
- Generates human-like text based on input.
- Predicts the next token repeatedly to generate responses.
- Examples: GPT, Claude, Gemini and Llama.

## 2. LLM in Agentic AI
LLMs act as the brain of AI agents.

They help with:
- Understanding user requests.
- Planning tasks.
- Making decisions.
- Generating responses.
- Choosing actions and tools.

## 3. API
- API = Application Programming Interface.
- Allows two applications to communicate.
- Our Python application sends requests to Groq and receives responses.

## 4. Tokens
- Small pieces of text processed by an LLM.
- Input and output usage are measured in tokens.
- Token usage affects API cost and context limits.

## 5. Temperature
Controls randomness in responses.
- Low temperature = More focused responses.
- High temperature = More creative responses.

## 6. Memory
- Individual API calls are stateless.
- Previous conversations are not automatically remembered.
- Applications must store and resend conversation history.

## 7. Context Window
- Maximum tokens a model can process in a request.
- Includes instructions, user input, history and generated output.

## 8. Hallucination
- When an LLM generates incorrect or made-up information.
- Providing reliable context and instructions can reduce hallucinations.

## 9. RAG
RAG = Retrieval-Augmented Generation.
- Retrieves relevant information from external sources.
- Provides that information to the LLM.
- Helps generate answers using supplied context.

## 10. First API Call

Used:
- OpenAI Python SDK.
- Groq API.
- `chat.completions.create()`

Important components:
- `model` - Selects the model.
- `temperature` - Controls randomness.
- `messages` - Contains system and user messages.
- `response.choices[0].message.content` - Gets the response.
- `response.usage` - Gets token usage information.