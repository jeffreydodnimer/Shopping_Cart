class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == price:
                entry['quantity'] += quantity
                return
        self.items.append({'name': name, 'quantity': quantity, 'price': price})

    def view_cart(self):
        return self.items

    def remove_item(self, name, quantity, price):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == price:
                if entry['quantity'] < quantity:
                    raise ValueError(f"Not enough {name} @ {price}")
                entry['quantity'] -= quantity
                if entry['quantity'] == 0:
                    self.items.remove(entry)
                return
        raise ValueError(f"No matching {name} @ {price} in cart.")

    def pay_items(self, items_to_pay):
        total = 0
        for item in items_to_pay:
            item_name = item['name']
            item_price = item['price']
            item_quantity = item['quantity']
            
            for entry in self.items:
                if entry['name'] == item_name and entry['price'] == item_price:
                    if entry['quantity'] < item_quantity:
                        raise ValueError(f"Not enough {item_name} @ {item_price}")
                    entry['quantity'] -= item_quantity
                    total += item_price * item_quantity
                    break
            else:
                raise ValueError(f"No matching {item_name} @ {item_price}")
        
        print(f"Total: ${total:.2f}")
        return total

    def update_item_name(self, old_name, old_price, new_name):
        for entry in self.items:
            if entry['name'] == old_name and entry['price'] == old_price:
                entry['name'] = new_name
                return
        raise ValueError(f"No matching {old_name} @ {old_price} to rename.")

    def update_item_quantity(self, name, price, new_quantity):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == price:
                entry['quantity'] = new_quantity
                return
        raise ValueError(f"No matching {name} @ {price} to change quantity.")

    def update_item_price(self, name, old_price, new_price):
        for entry in self.items:
            if entry['name'] == name and entry['price'] == old_price:
                entry['price'] = new_price
                return
        raise ValueError(f"No matching {name} @ {old_price} to change price.")
