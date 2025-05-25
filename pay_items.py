def run(cart):
    if not cart.items:
        print("🛒 Your cart is empty.")
        return

    print("\n💳 Pay for Items")
    for i, item in enumerate(cart.items, 1):
        print(f"{i}. {item['name'].title()} | Qty: {item['quantity']} | "
              f"P{item['price']:.2f}")

    total = 0
    while True:
        name = input("\nItem name (or 'done'): ").strip().lower()
        if name == 'done':
            break

        try:
            price = float(input("Price: "))
            qty = int(input("Qty: "))
            for item in cart.items:
                if item['name'] == name and item['price'] == price:
                    if item['quantity'] < qty:
                        print("❌ Not enough stock.")
                        break
                    item['quantity'] -= qty
                    total += qty * price
                    print(f"✅ Paid {qty} x {name} P{price:.2f}")
                    break
            else:
                print("❌ Item not found.")
        except:
            print("⚠️ Invalid input.")

    cart.items = [i for i in cart.items if i['quantity'] > 0]
    print(f"\n💰 Total: P{total:.2f}")
