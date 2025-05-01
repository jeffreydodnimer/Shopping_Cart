def run(cart):
    name  = input("Name to remove: ").strip().lower()
    try:
        price = float(input("Price of that line: "))
        qty   = int(input("Quantity to remove: "))
        cart.remove_item(name, qty, price)
        print(f"🗑️ Removed {qty}× {name} @ ${price:.2f}")
    except ValueError as e:
        print(f"⚠️ {e}")