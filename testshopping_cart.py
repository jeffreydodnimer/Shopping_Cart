import pytest
from shopping_cart import ShoppingCart

class TestShoppingCart:

    def setup_method(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("apple", 2, 1.5)
        assert self.cart.view_cart() == [{'name': 'apple', 'quantity': 2, 'price': 1.5}]

    def test_add_existing_item(self):
        self.cart.add_item("apple", 2, 1.5)
        self.cart.add_item("apple", 3, 1.5)
        assert self.cart.view_cart() == [{'name': 'apple', 'quantity': 5, 'price': 1.5}]

    def test_remove_item_partial(self):
        self.cart.add_item("banana", 4, 0.5)
        self.cart.remove_item("banana", 2, 0.5)
        assert self.cart.view_cart() == [{'name': 'banana', 'quantity': 2, 'price': 0.5}]

    def test_remove_item_exact(self):
        self.cart.add_item("milk", 2, 2.0)
        self.cart.remove_item("milk", 2, 2.0)
        assert self.cart.view_cart() == []

    def test_remove_item_not_found(self):
        with pytest.raises(ValueError, match="No matching item\\+price in cart."):
            self.cart.remove_item("eggs", 1, 1.0)

    def test_pay_items_partial(self):
        self.cart.add_item("apple", 5, 2.0)
        total = self.cart.pay_items([{'name': 'apple', 'price': 2.0, 'quantity': 3}])
        assert total == 6.0
        assert self.cart.view_cart() == [{'name': 'apple', 'quantity': 2, 'price': 2.0}]

    def test_pay_items_exact(self):
        self.cart.add_item("orange", 2, 3.0)
        total = self.cart.pay_items([{'name': 'orange', 'price': 3.0, 'quantity': 2}])
        assert total == 6.0
        assert self.cart.view_cart() == []

    def test_pay_items_too_much(self):
        self.cart.add_item("water", 1, 1.0)
        with pytest.raises(ValueError, match="Not enough water @ 1.0"):
            self.cart.pay_items([{'name': 'water', 'price': 1.0, 'quantity': 2}])

    def test_update_item_name(self):
        self.cart.add_item("bread", 1, 2.0)
        self.cart.update_item_name("bread", 2.0, "baguette")
        assert self.cart.view_cart() == [{'name': 'baguette', 'quantity': 1, 'price': 2.0}]

    def test_update_item_quantity(self):
        self.cart.add_item("soda", 2, 1.0)
        self.cart.update_item_quantity("soda", 1.0, 5)
        assert self.cart.view_cart() == [{'name': 'soda', 'quantity': 5, 'price': 1.0}]

    def test_update_item_price(self):
        self.cart.add_item("chips", 3, 1.5)
        self.cart.update_item_price("chips", 1.5, 2.0)
        assert self.cart.view_cart() == [{'name': 'chips', 'quantity': 3, 'price': 2.0}]

    def test_update_item_not_found(self):
        with pytest.raises(ValueError, match="No matching item\\+price to rename."):
            self.cart.update_item_name("cookie", 1.0, "biscuit")
        with pytest.raises(ValueError, match="No matching item\\+price to change quantity."):
            self.cart.update_item_quantity("cookie", 1.0, 5)
        with pytest.raises(ValueError, match="No matching item\\+price to change price."):
            self.cart.update_item_price("cookie", 1.0, 2.0)
