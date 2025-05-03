def run(cart):
    old_name = input("Which item name? ").strip().lower()
    old_price = float(input("Price of item to update: "))

    new_name = input("New name: ").strip().lower()
    new_quantity = int(input("New quantity: "))
    new_price = float(input("New price: "))

    try:
        cart.update_item_name(old_name, old_price, new_name)
        cart.update_item_price(new_name, old_price, new_price)
        cart.update_item_quantity(new_name, new_price, new_quantity)
        print(f"✅ Updated '{new_name}' to quantity {new_quantity} and price P{new_price:.2f}.")
    except ValueError as e:
        print(f"❌ {e}")
