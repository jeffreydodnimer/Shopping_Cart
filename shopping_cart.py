class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        for item in self.items:
            if item['name'] == name and item['price'] == price:
                item['quantity'] += quantity
                return
        self.items.append({'name': name, 'quantity': quantity, 'price': price})

    def remove_item(self, name, quantity, price):
        for item in self.items:
            if item['name'] == name and item['price'] == price:
                if item['quantity'] < quantity:
                    raise ValueError(f"Not enough {name} @ {price}")
                item['quantity'] -= quantity
                if item['quantity'] == 0:
                    self.items.remove(item)
                return
        raise ValueError(f"No matching {name} @ {price}")

    def update_item_name(self, name, price, new_name):
        for item in self.items:
            if item['name'] == name and item['price'] == price:
                item['name'] = new_name
                return
        raise ValueError(f"No matching {name} @ {price} to rename.")

    def update_item_quantity(self, name, price, new_quantity):
        for item in self.items:
            if item['name'] == name and item['price'] == price:
                item['quantity'] = new_quantity
                return
        raise ValueError(f"No matching {name} @ {price} to change quantity.")

    def update_item_price(self, name, price, new_price):
        for item in self.items:
            if item['name'] == name and item['price'] == price:
                item['price'] = new_price
                return
        raise ValueError(f"No matching {name} @ {price} to change price.")

    def view_cart(self):
        return self.items
