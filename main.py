from shopping_cart import ShoppingCart
import add_item
import remove_item
import view_cart
import pay_items
import update_item


def main():
    cart = ShoppingCart()
    print("🛒 Welcome to CLI Shopping Cart")

    actions = {
        '1': add_item.run,
        '2': remove_item.run,
        '3': view_cart.run,
        '4': pay_items.run,
        '6': update_item.run,
    }

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Pay")
        print("5. Exit")
        print("6. Update item")

        choice = input("Choose (1-6): ").strip()
        if choice == '5':
            print("👋 Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action(cart)
        else:
            print("⚠️ Invalid option. Choose 1–6.")

if __name__ == '__main__':
    main()
