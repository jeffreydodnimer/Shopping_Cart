def run(cart):
    print("\nCurrent Cart:")
    if not cart.items:
        print("Your cart is empty!")
        return
    for item in cart.items:
        print(f"  {item['name'].title()} — {item['quantity']}× @ ${item['price']:.2f} = "
              f"${item['quantity'] * item['price']:.2f}")
    print("\nTotal: ${:.2f}".format(sum(item['quantity'] * item['price'] for item in cart.items)))
