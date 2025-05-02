def run(cart):
    name = input("Which item name? ").strip().lower()
    price = float(input("Price of item to update: "))
    new_name = input("New name: ").strip().lower()
    new_quantity = int(input("New quantity: "))
    new_price = float(input("New price: "))

    cart.update_item_name(name, price, new_name)
    cart.update_item_quantity(new_name, new_price, new_quantity)
    cart.update_item_price(new_name, new_price, new_price)
    print(f"Updated {new_name} with quantity {new_quantity} and price {new_price}.")
