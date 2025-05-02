class ViewCart:
    def __init__(self):
        self.cart = []

    def add_item(self, name, quantity, price):
        for item in self.cart:
            if item['name'] == name and item['price'] == price:
                item['quantity'] += quantity
                return
        self.cart.append({'name': name, 'quantity': quantity, 'price': price})

    def remove_item(self, name, quantity, price):
        for item in self.cart:
            if item['name'] == name and item['price'] == price:
                if item['quantity'] > quantity:
                    item['quantity'] -= quantity
                elif item['quantity'] == quantity:
                    self.cart.remove(item)
                return
        raise ValueError("No matching item+price in cart.")

    def view_cart(self):
        return self.cart

    def pay_items(self, items):
        total = 0
        for item in items:
            for cart_item in self.cart:
                if cart_item['name'] == item['name'] and cart_item['price'] == item['price']:
                    if cart_item['quantity'] >= item['quantity']:
                        total += cart_item['price'] * item['quantity']
                        cart_item['quantity'] -= item['quantity']
                        if cart_item['quantity'] == 0:
                            self.cart.remove(cart_item)
                        break
                    else:
                        raise ValueError(
                            f"Not enough {cart_item['name']} @ {cart_item['price']}")
        return total
