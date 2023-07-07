
import surfshop
import unittest


class Testing(unittest.TestCase):

    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_surfboard(self):
        self.assertEqual(self.cart.add_surfboards(1), f'Successfully added 1 surfboard to cart!')

    def test_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                self.assertEqual(self.cart.add_surfboards(i), f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    @unittest.skip
    def test_error_boards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    # @unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def __str__(self):
        return 'Cart cannot have more than 4 surfboards in it!'


unittest.main()
