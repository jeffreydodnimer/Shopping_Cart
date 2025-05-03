def run(cart):
    if not cart.items:
        print("🛒 Your cart is empty.")
        return

    print("\n💳 Pay for Items")
    cart_items = cart.view_cart()

    # Display items
    print("Items in your cart:")
    for i, item in enumerate(cart_items, 1):
        print(f"{i}. {item['name'].title()} | Qty: {item['quantity']} | Price: P{item['price']:.2f}")

    total = 0
    while True:
        item_name = input("\nEnter item name to pay for (or 'done' to finish): ").strip().lower()
        if item_name == 'done':
            break

        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity to pay for: "))

            # Find item in cart
            for item in cart.items:
                if item['name'] == item_name and item['price'] == price:
                    if item['quantity'] < quantity:
                        print(f"❌ Not enough quantity for {item_name}.")
                        break
                    item['quantity'] -= quantity
                    total += quantity * price
                    print(f"✅ Paid for {quantity} x {item_name} P{price:.2f}")
                    break
            else:
                print(f"❌ Item '{item_name}'  P{price:.2f} not found.")
        except ValueError:
            print("⚠️ Invalid input. Please try again.")

    # Remove any items with 0 quantity
    cart.items = [item for item in cart.items if item['quantity'] > 0]

    print(f"\n💰 Total paid: P{total:.2f}")
