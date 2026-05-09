import unittest
from mean_var_std import calculate


class UnitTests(unittest.TestCase):

    def test_calculate(self):
        actual = calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])

        self.assertAlmostEqual(
            actual['variance'][2],
            6.987654320987654,
            places=5
        )

        self.assertAlmostEqual(
            actual['standard deviation'][2],
            2.6434171674156266,
            places=5
        )

        self.assertEqual(actual['max'][2], 8)
        self.assertEqual(actual['min'][2], 0)
        self.assertEqual(actual['sum'][2], 35)

    def test_calculate2(self):
        actual = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

        self.assertAlmostEqual(actual['mean'][2], 4.0, places=5)
        self.assertEqual(actual['max'][2], 8)
        self.assertEqual(actual['min'][2], 0)
        self.assertEqual(actual['sum'][2], 36)

    def test_calculate_fail(self):
        self.assertRaises(
            ValueError,
            lambda: calculate([2, 6, 2, 8, 4, 0, 1])
        )


if __name__ == "__main__":
    unittest.main()