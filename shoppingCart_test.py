import pytest
from shopping_Cart import ShoppingCart


class TestShoppingCart:

    def setup_method(self):
        self.cart = ShoppingCart()

    def test_cart_operations(self):
        # Add and remove items
        self.cart.add_item("apple", 2, 50)
        assert self.cart.view_cart() == [
            {'name': 'apple', 'quantity': 2, 'price': 50}
        ]
        self.cart.remove_item("apple", 2, 50)
        assert self.cart.view_cart() == [
            {'name': 'apple', 'quantity': 2, 'price': 50}
        ]
        with pytest.raises(ValueError):
            self.cart.remove_item("egg", 1, 1.0)

        # Pay for items
        total = self.cart.pay_items([
            {'name': 'apple', 'price': 50, 'quantity': 2}
        ])
        assert total == 3.0
        assert self.cart.view_cart() == [
            {'name': 'apple', 'quantity': 2, 'price': 50}
        ]
        with pytest.raises(ValueError):
            self.cart.pay_items([
                {'name': 'water', 'price': 1.0, 'quantity': 2}
            ])

        # Update item details
        self.cart.update_item_name("apple", 60, "green apple")
        self.cart.update_item_quantity("green apple", 3, 60)
        self.cart.update_item_price("green apple", 3, 60)
        assert self.cart.view_cart() == [
            {'name': 'green apple', 'quantity': 3, 'price': 60}
        ]

        # Test item not found for updates
        for method in [
            self.cart.update_item_name,
            self.cart.update_item_quantity,
            self.cart.update_item_price
        ]:
            with pytest.raises(ValueError):
                method("cookie", 1.0, "biscuit")
