def run(cart):
    items = cart.view_cart()
    if not items:
        print("🧺 Nothing to pay.")
        return

    print("🧾 Cart items:")
    for e in items:
        print(f"  {e['name'].title()} — {e['quantity']}× @ ${e['price']:.2f} = ${e['quantity'] * e['price']:.2f}")

    to_pay = []
    while True:
        nm = input("Item to pay for (or 'done'): ").strip().lower()
        if nm == 'done':
            break
        try:
            pr = float(input("  Price of that line: "))
            qt = int(input("  Quantity: "))
            to_pay.append({'name': nm, 'price': pr, 'quantity': qt})
        except ValueError:
            print("⚠️ Invalid input.")

    try:
        total = cart.pay_items(to_pay)
        print(f"💰 Paid total: ${total:.2f}")
    except ValueError as e:
        print(f"⚠️ {e}")