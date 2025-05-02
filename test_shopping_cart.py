import pytest
from shopping_cart import ShoppingCart

class TestShoppingCart(pytest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("apple", 2, 1.5)
        self.assertEqual(self.cart.view_cart(), {"apple": (2, 1.5)})

    def test_add_existing_item(self):
        self.cart.add_item("apple", 2, 1.5)
        self.cart.add_item("apple", 3, 1.5)
        self.assertEqual(self.cart.view_cart(), {"apple": (5, 1.5)})

    def test_remove_item_partial(self):
        self.cart.add_item("banana", 4, 0.5)
        self.cart.remove_item("banana", 2)
        self.assertEqual(self.cart.view_cart(), {"banana": (2, 0.5)})

    def test_remove_item_exact(self):
        self.cart.add_item("milk", 2, 2.0)
        self.cart.remove_item("milk", 2)
        self.assertNotIn("milk", self.cart.view_cart())

    def test_remove_item_too_much(self):
        self.cart.add_item("bread", 1, 1.0)
        with self.assertRaises(ValueError) as context:
            self.cart.remove_item("bread", 2)
        self.assertEqual(str(context.exception), "Too much quantity you entered.")

    def test_remove_item_not_found(self):
        with self.assertRaises(ValueError) as context:
            self.cart.remove_item("eggs", 1)
        self.assertEqual(str(context.exception), "Item not in cart.")

    def test_pay_items_partial(self):
        self.cart.add_item("apple", 5, 2.0)  # $10.00
        paid = self.cart.pay_items({"apple": 3})  # Pay for 3 only
        self.assertEqual(paid, 6.0)
        self.assertEqual(self.cart.view_cart(), {"apple": (2, 2.0)})

    def test_pay_items_exact(self):
        self.cart.add_item("orange", 2, 3.0)
        paid = self.cart.pay_items({"orange": 2})
        self.assertEqual(paid, 6.0)
        self.assertEqual(self.cart.view_cart(), {})

    def test_pay_items_too_much(self):
        self.cart.add_item("water", 1, 1.0)
        with self.assertRaises(ValueError):
            self.cart.pay_items({"water": 2})

if __name__ == '__main__':
    pytest.main()
