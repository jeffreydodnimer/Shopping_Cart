class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.paid = False

    def add_item(self, item, price):
        self.cart.append({'item': item, 'price': price})

    def remove_item(self, item):
        self.cart = [i for i in self.cart if i['item'] != item]

    def check_cart(self):
        return self.cart

    def total_price(self):
        return sum(item['price'] for item in self.cart)

    def pay(self):
        if not self.cart:
            raise Exception("Cart is empty. Cannot proceed to payment.")
        self.paid = True
        return f"Payment successful. Total paid: ${self.total_price():.2f}"
