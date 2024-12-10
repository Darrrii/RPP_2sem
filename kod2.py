def calculate_total(order):
    total = sum(item["price"] * item["quantity"] for item in order["items"])
    return total

def process_payment():
    print("Processing payment...")
    print("Payment successful!")

def send_confirmation():
    print("Sending confirmation email...")
    print("Order complete.")

def process_order(order):
    total = calculate_total(order)
    print(f"Total: {total}")
    process_payment()
    send_confirmation()

if __name__ == "__main__":
    # Пример заказа
    order = {
        "items": [
            {"price": 10.0, "quantity": 2},  # 2 товара по 10.0
            {"price": 5.0, "quantity": 1}    # 1 товар по 5.0
        ]
    }
    
    process_order(order)
