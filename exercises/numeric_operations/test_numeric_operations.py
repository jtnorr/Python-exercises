import unittest

from exercises.numeric_operations.numeric_operations_exercises import (
    calculate_series_sum,
    is_prime,
    get_fibonacci_sequence,
    multiply_table
)


class TestNumericOperations(unittest.TestCase):

    def test_calculate_series_sum(self):
        self.assertEqual(calculate_series_sum(5), 15)
        self.assertEqual(calculate_series_sum(1), 1)
        self.assertEqual(calculate_series_sum(10), 55)
        with self.assertRaises(ValueError):
            calculate_series_sum(0)
            calculate_series_sum(-1)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))

    def test_fibonacci_sequence(self):
        self.assertEqual(get_fibonacci_sequence(1), [0])
        self.assertEqual(get_fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(get_fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])
        with self.assertRaises(ValueError):
            get_fibonacci_sequence(0)

    def test_multiply_table(self):
        self.assertEqual(multiply_table(2), [[1, 2], [2, 4]])
        self.assertEqual(multiply_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
        with self.assertRaises(ValueError):
            multiply_table(0)

if __name__ == '__main__':
    unittest.main(verbosity=2)