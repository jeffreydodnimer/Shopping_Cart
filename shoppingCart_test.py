import unittest
from shopping_Cart import ShoppingCart


class TestCart(unittest.TestCase):
    def test_cart_actions(self):
        cart = ShoppingCart()
        cart.add_item("Book", 10)
        cart.add_item("Pen", 2)
        self.assertEqual(len(cart.check_cart()), 2)

        cart.remove_item("Pen")
        self.assertEqual(len(cart.check_cart()), 1)

        self.assertEqual(cart.total_price(), 10)

        msg = cart.pay()
        self.assertTrue(cart.paid)
        self.assertIn("Paid", msg)

    def test_pay_empty(self):
        with self.assertRaises(Exception):
            ShoppingCart().pay()


if __name__ == '__main__':
    unittest.main()
