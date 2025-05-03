def run(cart):
    try:
        old_name = input("Old name: ").strip().lower()
        old_price = float(input("Old price: "))
        new_name = input("New name: ").strip().lower()
        new_qty = int(input("New quantity: "))
        new_price = float(input("New price: "))

        cart.update_item_name(old_name, old_price, new_name)
        cart.update_item_price(new_name, old_price, new_price)
        cart.update_item_quantity(new_name, new_price, new_qty)

        print(f"✅ Updated '{new_name}' to {new_qty} pcs @ P{new_price:.2f}")
    except ValueError as e:
        print(f"❌ {e}")
