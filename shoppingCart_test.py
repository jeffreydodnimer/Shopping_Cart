import unittest
from shopping_Cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_and_remove_items(self):
        self.cart.add_item("apple", 2, 50)
        self.cart.add_item("apple", 3, 50)
        self.assertEqual(self.cart.view_cart(), [
            {'name': 'apple', 'quantity': 5, 'price': 50}
        ])

        self.cart.remove_item("apple", 3, 1.5)
        self.assertEqual(self.cart.view_cart(), [
            {'name': 'apple', 'quantity': 2, 'price': 1.5}
        ])

        with self.assertRaises(ValueError):
            self.cart.remove_item("egg", 1, 1.0)

    def test_pay_items(self):
        self.cart.add_item("apple", 2, 1.5)
        total = self.cart.pay_items([
            {'name': 'apple', 'price': 1.5, 'quantity': 2}
        ])
        self.assertEqual(total, 3.0)
        self.assertEqual(self.cart.view_cart(), [
            {'name': 'apple', 'quantity': 0, 'price': 1.5}
        ])

        with self.assertRaises(ValueError):
            self.cart.pay_items([
                {'name': 'water', 'price': 1.0, 'quantity': 2}
            ])

    def test_update_item(self):
        self.cart.add_item("apple", 2, 1.5)
        self.cart.update_item_name("apple", 1.5, "green apple")
        self.cart.update_item_quantity("green apple", 1.5, 3)
        self.cart.update_item_price("green apple", 1.5, 2.0)
        self.assertEqual(self.cart.view_cart(), [
            {'name': 'green apple', 'quantity': 3, 'price': 2.0}
        ])

        with self.assertRaises(ValueError):
            self.cart.update_item_name("cookie", 1.0, "biscuit")
        with self.assertRaises(ValueError):
            self.cart.update_item_quantity("cookie", 1.0, 5)
        with self.assertRaises(ValueError):
            self.cart.update_item_price("cookie", 1.0, 2.0)


if __name__ == '__main__':
    unittest.main()
