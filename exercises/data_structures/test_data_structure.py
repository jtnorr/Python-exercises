"""
Unit tests for data structures exercises
"""

import unittest

from exercises.data_structures.data_structure_exercises import (
    filter_and_sort_list,
    merge_dictionaries,
    group_by_type,
    rotate_matrix
)


class TestDataStructures(unittest.TestCase):
    """Unit tests for data structures exercises"""

    def test_filter_and_sort_list(self):
        """Test filter_and_sort_list function"""
        self.assertEqual(filter_and_sort_list([3, -1, 4, -5, 2, -2]), [2, 3, 4])
        self.assertEqual(filter_and_sort_list([-1, -2, -3]), [])
        self.assertEqual(filter_and_sort_list([]), [])

    def test_merge_dictionaries(self):
        """Test merge_dictionaries function"""
        self.assertEqual(
            merge_dictionaries(
                {'a': 1, 'b': 2, 'c': 'hello'},
                {'b': 3, 'c': ' world', 'd': 4}
            ),
            {'a': 1, 'b': 5, 'c': 'hello world', 'd': 4}
        )
        self.assertEqual(
            merge_dictionaries({'a': 1}, {'b': 2}),
            {'a': 1, 'b': 2}
        )
        self.assertEqual(
            merge_dictionaries({}, {'a': 1}),
            {'a': 1}
        )

    def test_group_by_type(self):
        """Test group_by_type function"""
        self.assertEqual(
            group_by_type([1, 'hello', 3.14, 'world', 42, 2.71]),
            {
                'int': [1, 42],
                'str': ['hello', 'world'],
                'float': [3.14, 2.71]
            }
        )
        self.assertEqual(
            group_by_type([1, 2, 3]),
            {'int': [1, 2, 3]}
        )
        self.assertEqual(
            group_by_type([]),
            {}
        )

    def test_rotate_matrix(self):
        """Test rotate_matrix function"""
        self.assertEqual(
            rotate_matrix([[1, 2], [3, 4]]),
            [[3, 1], [4, 2]]
        )
        self.assertEqual(
            rotate_matrix([[1]]),
            [[1]]
        )
        self.assertEqual(
            rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
