def run(cart):
    if not cart.items:
        print("🛒 Your cart is empty.")
        return

    try:
        name = input("Name to remove: ").strip().lower()
        quantity = int(input("Quantity to remove: "))
        price = float(input("Price of item to remove: "))

        for entry in cart.items:
            if entry['name'] == name and entry['price'] == price:
                if entry['quantity'] < quantity:
                    print(f"❌ Not enough quantity of {name} at P{price:.2f}.")
                    return
                entry['quantity'] -= quantity
                if entry['quantity'] == 0:
                    cart.items.remove(entry)
                print(f"✅ Removed {quantity} x {name} P{price:.2f}")
                return

        print(f"❌ No matching item '{name}' P{price:.2f} found in cart.")
    except ValueError:
        print("⚠️ Invalid input. Please enter correct number and price formats.")
