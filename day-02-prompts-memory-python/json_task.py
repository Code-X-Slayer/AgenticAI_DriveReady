import json
from config import ORDER_EXTRACTION_SYSTEM
from experiment import get_messages_template,  get_response_with_messages
from order import get_bill, extract_order

messages = get_messages_template(system_prompt=ORDER_EXTRACTION_SYSTEM)

queries = [
   "I need 2 plum cakes and 3 cupcakes.",
   "I need 2 vanilla cakes.",
   "I need 2 plum cakes and 1 vanilla cake.",
   "I need cupcakes." 
]

for query in queries:
    print(f"Query: {query}")
    try:
        data = extract_order(query)
        bill = get_bill(data)
        print(f"Data: {data}")
        print(f"Bill: {bill}")
    except Exception as e:
        print(f"Error processing query '{query}': {e}")

# Query: I need 2 plum cakes and 3 cupcakes.
# Response: {"category":"order","items":[{"item":"plum cake","quantity":2},{"item":"cupcake","quantity":3}]}
# Data: {'category': 'order', 'items': [{'item': 'plum cake', 'quantity': 2}, {'item': 'cupcake', 'quantity': 3}]}
# Bill: {'items': ['order_item: plum cake, quantity: 2, subtotal: 1000', 'order_item: cupcake, quantity: 3, subtotal: 240'], 'total': 1240, 'invalid_items': []}
# Query: I need 2 vanilla cakes.
# Response: {
#     "category": "order",
#     "items": [
#         {
#             "item": "vanilla cake",
#             "quantity": 2
#         }
#     ]
# }
# Data: {'category': 'order', 'items': [{'item': 'vanilla cake', 'quantity': 2}]}
# Bill: {'items': [], 'total': 0, 'invalid_items': [{'item': 'vanilla cake', 'quantity': 2}]}
# Query: I need 2 plum cakes and 1 vanilla cake.
# Response: {"category":"order","items":[{"item":"plum cake","quantity":2},{"item":"vanilla cake","quantity":1}]}
# Data: {'category': 'order', 'items': [{'item': 'plum cake', 'quantity': 2}, {'item': 'vanilla cake', 'quantity': 1}]}
# Bill: {'items': ['order_item: plum cake, quantity: 2, subtotal: 1000'], 'total': 1000, 'invalid_items': [{'item': 'vanilla cake', 'quantity': 1}]}
# Query: I need cupcakes.
# Response: {"category":"order","items":[{"item":"cupcake","quantity":null}]}
# Data: {'category': 'order', 'items': [{'item': 'cupcake', 'quantity': None}]}
# Bill: {'items': [], 'total': 0, 'invalid_items': [{'item': 'cupcake', 'quantity': None}]}
# (.venv) vijay@VIJAY-KARTHIK:~/git/AgenticAI_DriveReady/day-02-prompts-memory-python$ 