// ```python
import unittest

from my_code import add


class TestAdd(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
// ```