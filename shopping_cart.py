class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == price:
                entry['quantity'] += quantity
                return
        self.items.append({'name': name, 'quantity': quantity, 'price': price})

    def remove_item(self, name, quantity, price):
        for i, entry in enumerate(self.items):
            if entry['name'] == name and entry['price'] == price:
                if quantity >= entry['quantity']:
                    # remove the whole line
                    self.items.pop(i)
                else:
                    entry['quantity'] -= quantity
                return
        raise ValueError("No matching item+price in cart.")

    def view_cart(self):
        return [dict(e) for e in self.items]

    def pay_items(self, to_pay):
        """
        to_pay: list of dicts [{'name': str, 'price': float, 'quantity': int}, ...]
        """
        total = 0.0
        for sel in to_pay:
            name = sel['name']
            price = sel['price']
            qty   = sel['quantity']
            # find the line
            for i, entry in enumerate(self.items):
                if entry['name'] == name and entry['price'] == price:
                    if qty > entry['quantity']:
                        raise ValueError(f"Not enough {name} @ {price}")
                    total += qty * price
                    # remove or decrement
                    if qty == entry['quantity']:
                        self.items.pop(i)
                    else:
                        entry['quantity'] -= qty
                    break
            else:
                raise ValueError(f"{name} @ {price} not in cart.")
        return total

    def update_item_name(self, name, price, new_name):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == price:
                entry['name'] = new_name
                return
        raise ValueError("No matching item+price to rename.")

    def update_item_quantity(self, name, price, new_qty):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == price:
                entry['quantity'] = new_qty
                return
        raise ValueError("No matching item+price to change quantity.")

    def update_item_price(self, name, price, new_price):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == price:
                qty = entry['quantity']
                self.items.remove(entry)
                for other in self.items:
                    if other['name'] == name and other['price'] == new_price:
                        other['quantity'] += qty
                        return
                self.items.append({'name': name, 'quantity': qty, 'price': new_price})
                return
        raise ValueError("No matching item+price to change price.")