def run(cart):
    name  = input("Which item name? ").strip().lower()
    try:
        price = float(input("Price of that line: "))
    except ValueError:
        print("⚠️ Invalid price.")
        return

    print("1. Rename  2. Change quantity  3. Change price")
    sub = input("Choose (1–3): ").strip()
    try:
        if sub == '1':
            new = input("New name: ").strip().lower()
            cart.update_item_name(name, price, new)
            print(f"🔄 Renamed to '{new}'")
        elif sub == '2':
            newq = int(input("New quantity: "))
            cart.update_item_quantity(name, price, newq)
            print(f"🔄 Quantity → {newq}")
        elif sub == '3':
            newp = float(input("New price: "))
            cart.update_item_price(name, price, newp)
            print(f"🔄 Price → ${newp:.2f}")
        else:
            print("⚠️ Invalid option.")
    except ValueError as e:
        print(f"⚠️ {e}")
