class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        for item in self.items:
            if item['name'] == name and item['price'] == price:
                item['quantity'] += quantity
                return
        self.items.append({
            'name': name,
            'quantity': quantity,
            'price': price
        })

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
        return self.items

    def pay_items(self, payment_items):
        total = 0.0
        for payment in payment_items:
            for item in self.items:
                if (item['name'] == payment['name'] and
                        item['price'] == payment['price']):
                    if payment['quantity'] > item['quantity']:
                        raise ValueError(
                            f"Not enough quantity of '{item['name']}' in cart."
                        )
                    item['quantity'] -= payment['quantity']
                    total += payment['quantity'] * payment['price']
                    if item['quantity'] == 0:
                        self.items.remove(item)
                    break
            else:
                raise ValueError(
                    f"Item '{payment['name']}' not found in cart."
                )
        return total
