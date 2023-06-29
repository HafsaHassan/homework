import unittest
from shop import purchase, greeting


class ShopProgramTests(unittest.TestCase):
    def test_purchase_affordable_item(self):
        self.assertTrue(purchase("book", 20))

    def test_purchase_unaffordable_item(self):
        self.assertFalse(purchase("bracelet", 50))

    def test_greeting_exit(self):
        self.assertEqual(greeting(), "Thanks for coming to our shop!")

    def test_greeting_valid_item(self):
        self.assertEqual(greeting(), "Here's your book! Goodbye.\n")

    def test_greeting_invalid_item(self):
        with self.assertRaises(ValueError):
            greeting()


if __name__ == '__main__':
    unittest.main()
