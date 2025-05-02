import pytest
from Shopping_Cart import ShoppingCart


class TestShoppingCart:

    def setup_method(self):
        self.cart = ShoppingCart()

    def test_cart_operations(self):
        # Add and remove items
        self.cart.add_item("apple", 2, 1.5)
        self.cart.add_item("apple", 3, 1.5)
        assert self.cart.view_cart() == [
            {'name': 'apple', 'quantity': 5, 'price': 1.5}
        ]
        self.cart.remove_item("apple", 3, 1.5)
        assert self.cart.view_cart() == [
            {'name': 'apple', 'quantity': 2, 'price': 1.5}
        ]
        with pytest.raises(ValueError):
            self.cart.remove_item("egg", 1, 1.0)

        # Pay for items
        total = self.cart.pay_items([
            {'name': 'apple', 'price': 1.5, 'quantity': 2}
        ])
        assert total == 3.0
        assert self.cart.view_cart() == [
            {'name': 'apple', 'quantity': 0, 'price': 1.5}
        ]
        with pytest.raises(ValueError):
            self.cart.pay_items([
                {'name': 'water', 'price': 1.0, 'quantity': 2}
            ])

        # Update item details
        self.cart.update_item_name("apple", 1.5, "green apple")
        self.cart.update_item_quantity("green apple", 1.5, 3)
        self.cart.update_item_price("green apple", 1.5, 2.0)
        assert self.cart.view_cart() == [
            {'name': 'green apple', 'quantity': 3, 'price': 2.0}
        ]

        # Test item not found for updates
        for method in [
            self.cart.update_item_name,
            self.cart.update_item_quantity,
            self.cart.update_item_price
        ]:
            with pytest.raises(ValueError):
                method("cookie", 1.0, "biscuit")
