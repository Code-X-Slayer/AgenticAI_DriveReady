from experiment import get_response_with_messages, get_messages_template

user_queries = [
    "My name is Vijay.",
    "I want 2 plum cakes.",
    "Whats my name and what did I order?"
]

messages = get_messages_template()

for query in user_queries:
    response = get_response_with_messages(messages, query)
    print(f"Query: {query}")
    print(f"Response: {response}")

# Query: My name is Vijay.
# Response: Hi Vijay! 👋 How can Sweet Crumbs help you today?
# Query: I want 2 plum cakes.
# Response: Sure thing, Vijay! 🎂 You’d like 2 plum cakes. We need a 24‑hour notice before baking, and all our cakes have eggless versions. The total would be ₹1,000. Let me know if that works, and we’ll lock it in!
# Query: Whats my name and what did I order?
# Response: Your name is Vijay, and you ordered two plum cakes.