def pay_items(cart, items_to_pay):
    total = 0
    for item in items_to_pay:
        item_name = item['name']
        item_price = item['price']
        item_quantity = item['quantity']
        
        for entry in cart.items:
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
