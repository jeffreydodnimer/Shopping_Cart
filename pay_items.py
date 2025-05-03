def run(cart):
    if not cart.items:
        print("🛒 Your cart is empty.")
        return

    print("\n💳 Pay for Items\nItems in your cart:")
    for i, item in enumerate(cart.items, 1):
        print(f"{i}. {item['name'].title()} | Qty: {item['quantity']} | Price: P{item['price']:.2f}")

    total = 0
    while True:
        name = input("\nEnter item name to pay for (or 'done' to finish): ").strip().lower()
        if name == 'done':
            break
        try:
            price = float(input("Enter item price: "))
            qty = int(input("Enter quantity to pay for: "))
            for item in cart.items:
                if item['name'] == name and item['price'] == price:
                    if item['quantity'] < qty:
                        print(f"❌ Not enough quantity for {name}.")
                        break
                    item['quantity'] -= qty
                    total += qty * price
                    print(f"✅ Paid for {qty} x {name} @ P{price:.2f}")
                    break
            else:
                print(f"❌ Item '{name}' @ P{price:.2f} not found.")
        except ValueError:
            print("⚠️ Invalid input.")

    cart.items = [item for item in cart.items if item['quantity'] > 0]
    print(f"\n💰 Total paid: P{total:.2f}")
