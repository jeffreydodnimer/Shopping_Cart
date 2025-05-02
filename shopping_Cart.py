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
                if quantity >= item['quantity']:
                    self.items.remove(item)
                else:
                    item['quantity'] -= quantity
                return
        raise ValueError(f"Item '{name}' not found in cart.")

    def view_cart(self):
        # Remove items with zero quantity
        self.items = [item for item in self.items if item['quantity'] > 0]
        return self.items

    def pay_items(self, payment_items):
        total = 0.0
        for payment in payment_items:
            for item in self.items:
                if item['name'] == payment['name'] and item['price'] == payment['price']:
                    if payment['quantity'] > item['quantity']:
                        raise ValueError(f"Not enough quantity of '{item['name']}' in cart.")
                    item['quantity'] -= payment['quantity']
                    total += payment['quantity'] * payment['price']
                    if item['quantity'] == 0:
                        self.items.remove(item)  # Remove item if quantity is zero
                    break
            else:
                raise ValueError(f"Item '{payment['name']}' not found in cart.")
        return total

    def update_item_name(self, old_name, old_price, new_name):
        for item in self.items:
            if item['name'] == old_name and item['price'] == old_price:
                item['name'] = new_name
                return
        raise ValueError(f"Item '{old_name}' not found for update.")

    def update_item_quantity(self, name, price, new_quantity):
        for item in self.items:
            if item['name'] == name and item['price'] == price:
                item['quantity'] = new_quantity
                return
        raise ValueError(f"Item '{name}' not found for update.")

    def update_item_price(self, name, old_price, new_price):
        for item in self.items:
            if item['name'] == name and item['price'] == old_price:
                item['price'] = new_price
                return
        raise ValueError(f"Item '{name}' with price '{old_price}' not found for update.")
