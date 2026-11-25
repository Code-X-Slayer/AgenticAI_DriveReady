from experiment import get_messages_template, get_response_with_messages
from classifier_zero_few_shot import classify_message
from order import extract_order, get_bill

def main():
    messages = get_messages_template()
    while True:
        query = input("user: ").strip().lower()
        if query == "exit":
            print(f"Exiting ...")
            break
        category = classify_message(query)
        if category == "order":
            data = extract_order(query)
            if not data["items"]:
                print(  f"assistant: I'm sorry, I couldn't extract any valid items from your order. Please clarify your order.")
                continue
            bill = get_bill(data)
            print(f"assistant: order summary")
            for item in bill['items']:
                print(f"{item["item"]} - {item["quantity"]} - {item["subtotal"]}/-")
            print(f"total: {bill['total']}")  # Assuming each item costs $5
            if bill['invalid_items']:
                print("please clarify these below items")
                for item in bill["invalid_items"]:
                    print(f"{item["item"]} - {item["quantity"]}")

        elif category == "question":
            response = get_response_with_messages(messages, query)
            print(f"assistant: {response}")
        elif category == "complaint":
            response = get_response_with_messages(messages, query)
            print(f"assistant: {response}")
        else:
            print(f"assistant: I'm sorry, I didn't understand that. Could you please clarify?")

if __name__ == "__main__":
    main()