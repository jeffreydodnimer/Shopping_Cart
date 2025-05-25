def run(cart):
    items = cart.view_cart()
    if not items:
        print("🧺 Cart is empty.")
    else:
        print("🧾 Cart:")
        total = 0
        for i in items:
            sub = i['quantity'] * i['price']
            total += sub
            print(f"{i['name'].title()} x{i['quantity']} @P{i['price']:.2f}")
            print(f"  = P{sub:.2f}")
        print(f"\nTotal: P{total:.2f}")
