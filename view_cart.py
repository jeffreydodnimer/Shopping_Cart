def run(cart):
    items = cart.view_cart()
    if not items:
        print("🧺 Your cart is empty.")
    else:
        print("🧾 Cart contents:")
        grand_total = 0.0
        for e in items:
            line_total = e['quantity'] * e['price']
            grand_total += line_total
            print(
                f"  {e['name'].title()} — {e['quantity']}× @ ${e['price']:.2f} = "
                f"${line_total:.2f}"
            )
        print(f"\nGrand total: ${grand_total:.2f}")
