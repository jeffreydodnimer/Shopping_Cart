def run(cart):
    name  = input("Enter item name: ").strip().lower()
    try:
        qty   = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        cart.add_item(name, qty, price)
        print(f"✅ Added {qty}× {name} @ ${price:.2f}")
    except ValueError:
        print("⚠️ Invalid quantity or price.")
