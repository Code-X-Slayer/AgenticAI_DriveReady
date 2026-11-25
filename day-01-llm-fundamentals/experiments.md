# Day 01 - Experiments

All experiments were performed using Groq API and `openai/gpt-oss-20b`.

## Experiment 1: Temperature Comparison

Compared temperature 0.2 and 1.2 using the same bakery question.

**Observation:**
- 0.2 generated a direct and concise response.
- 1.2 generated a more formatted and expressive response.
- Both followed the provided bakery facts.

**Learning:** Temperature influences response variation and creativity.

## Experiment 2: Hallucination Testing

Asked for the price of a vanilla cake.

**Test 1:** Provided complete bakery facts and rules.

Response:
"I'll check with the owner."

**Test 2:** Removed business facts and rules.

Response:
The model invented vanilla cake prices, sizes and additional charges in dollars.

**Learning:**
- Providing business facts helps prevent unsupported answers.
- Without reliable context, the model may invent information.
- Missing information should be handled carefully.

Note: Both the context and temperature were changed in this experiment, so this was not a controlled comparison of context alone.

## Experiment 3: Conversation History

**Test 1:** First API call asked for available cakes. Second API call included the previous conversation.

**Test 2:** The second request included the previous assistant response and the new user question.

**Observation:**
- The second request successfully answered the follow-up question using previous conversation history.
- Conversation history must be included in subsequent API requests.

**Learning:** API calls are stateless. Applications need to maintain and resend conversation history for memory.

## Experiment 4: English vs Telugu Token Usage

Asked the same bakery question in English and Telugu.

| Language | Completion Tokens |
|---|---:|
| English | 338 |
| Telugu | 562 |

**Observation:**
- Telugu response used more completion tokens than English in this experiment.
- Both responses provided the same bakery information.

**Learning:** Token usage can vary depending on the language and generated response.

## Final Takeaways

1. Temperature affects response variation.
2. Providing facts and rules helps reduce hallucinations.
3. Conversation history must be passed to maintain context.
4. Different languages can have different token usage.

## Status

- [x] Temperature comparison
- [x] Hallucination experiment
- [x] Conversation history experiment
- [x] English vs Telugu token comparison