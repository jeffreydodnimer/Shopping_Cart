def run(cart):
    name = input("Name to remove: ").strip().lower()
    quantity = int(input("Quantity to remove: "))
    price = float(input("Price of item to remove: "))

    for entry in cart.items:
        if entry['name'] == name and entry['price'] == price:
            if entry['quantity'] < quantity:
                raise ValueError(f"Not enough {name} @ {price}")
            entry['quantity'] -= quantity
            if entry['quantity'] == 0:
                cart.items.remove(entry)
            return
    raise ValueError(f"No matching {name} @ {price} in cart.")
