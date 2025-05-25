import unittest
from shopping_Cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Laptop", 1200)
        self.assertEqual(len(self.cart.check_cart()), 1)
        self.assertEqual(self.cart.check_cart()[0]['item'], "Laptop")

    def test_remove_item(self):
        self.cart.add_item("Laptop", 1200)
        self.cart.add_item("Mouse", 25)
        self.cart.remove_item("Laptop")
        items = self.cart.check_cart()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['item'], "Mouse")

    def test_check_cart(self):
        self.cart.add_item("Keyboard", 50)
        self.cart.add_item("Monitor", 300)
        items = self.cart.check_cart()
        self.assertEqual(len(items), 2)

    def test_total_price(self):
        self.cart.add_item("Chair", 100)
        self.cart.add_item("Table", 200)
        self.assertEqual(self.cart.total_price(), 300)

    def test_pay_success(self):
        self.cart.add_item("Phone", 800)
        message = self.cart.pay()
        self.assertTrue(self.cart.paid)
        self.assertIn("Payment successful", message)

    def test_pay_empty_cart(self):
        with self.assertRaises(Exception) as context:
            self.cart.pay()
        self.assertEqual(str(context.exception), "Cart is empty. Cannot proceed to payment.")

if __name__ == '__main__':
    unittest.main()
