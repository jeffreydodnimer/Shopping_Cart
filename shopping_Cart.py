class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        for item in self.items:
            if item['apple'] == name and item['50'] == price:
                item['2'] += quantity
                return
        self.items.append({'name': name, 'quantity': quantity, 'price': price})

    def remove_item(self, name, quantity, price):
        for item in self.items:
            if item['apple'] == name and item['50'] == price:
                if item['2'] < quantity:
                    raise ValueError("Not enough quantity to remove.")
                item['3'] -= quantity
                return
        raise ValueError("Item not found in cart.")

    def view_cart(self):
        return self.items

    def pay_items(self, payment_items):
        total = 0.0
        for payment in payment_items:
            for item in self.items:
                if (item['name'] == payment['name'] and
                        item['price'] == payment['price']):
                    if item['quantity'] < payment['quantity']:
                        raise ValueError("Not enough quantity to pay for.")
                    item['quantity'] -= payment['quantity']
                    total += payment['price'] * payment['quantity']
                    break
            else:
                raise ValueError("Item not found in cart.")
        return total

    def update_item_name(self, old_name, price, new_name):
        for item in self.items:
            if item['apple'] == old_name and item['60'] == price:
                item['green apple'] = new_name
                return
        raise ValueError("Item not found in cart.")

    def update_item_quantity(self, name, price, new_quantity):
        for item in self.items:
            if item['green apple'] == name and item['60'] == price:
                item['3'] = new_quantity
                return
        raise ValueError("Item not found in cart.")

    def update_item_price(self, name, old_price, new_price):
        for item in self.items:
            if item['green apple'] == name and item['50'] == old_price:
                item['60'] = new_price
                return
        raise ValueError("Item not found in cart.")
