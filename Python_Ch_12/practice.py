orders = [
    {"id": 101, "customer": "Alice", "items": ["A1", "B2"], "total": "450"},
    {"id": 102, "customer": "Bob", "items": ["C3"], "total": 390},
    {"id": 103, "customer": "Carol", "items": ["D4"], "total": 510},
    {"id": 104, "customer": "David", "items": ["E5"], "total": "invalid"},
    {"id": 105, "items": ["F6"], "total": 200}
]

inventory = {
    "A1": {"price": 200, "stock": 10},
    "B2": {"price": 250, "stock": 0},
    "C3": {"price": 180, "stock": 5},
    "D4": {"price": 510, "stock": 2},
    "E5": {"price": None, "stock": 3},
    "F6": {"stock": 4}
}

payments = {
    101: 450,
    102: 380,
    103: "510",
    104: 500,
    106: 200
}

def process_orders(orders, inventory, payments):
    for order in orders:
        customer = order["customer"]
        print(f"Processing order for {customer}")

        items = order["items"]
        order_total = float(order["total"])

        calculated_total = 0
        for item in items:
            item_info = inventory[item]
            price = item_info["price"]
            calculated_total += price

        payment_received = payments[order["id"]]

        # if payment_received < calculated_total:
        #     print("Payment insufficient.")
        # elif payment_received > calculated_total:
        #     raise ValueError("Overpayment detected")
        # else:
        #     print("Payment successful.")

        # if item_info["stock"] < 1:
        #     print(f"Item {item} out of stock")
        # else:
        #     inventory[item]["stock"] -= 1

        print(f"Order {order['id']} completed.\n")

def generate_summary(orders):
    customers = [o["customer"] for o in orders]
    total_orders = len(customers)
    unique_customers = set(customers)
    print("Total orders:", total_orders)
    print("Unique customers:", len(unique_customers))

    totals = [float(o["total"]) for o in orders]
    avg = sum(totals) / len(totals)
    print("Average order value:", avg)

    print("Max order value:", max(totals))
    print("Min order value:", min(totals))

def product_report(inventory):
    for product_id in inventory:
        price = inventory[product_id]["price"]
        if price > 500:
            print(f"Premium Product: {product_id}")
        elif price < 200:
            print(f"Budget Product: {product_id}")
        else:
            print(f"Mid-range Product: {product_id}")

process_orders(orders, inventory, payments)
generate_summary(orders)
product_report(inventory)