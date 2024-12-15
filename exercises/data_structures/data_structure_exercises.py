"""
Assignment: Data Structures and Manipulation

This assignment focuses on:
- Lists and list operations
- Dictionaries
- Data transformation
- Working with complex data structures
"""


def filter_and_sort_list(numbers: list) -> list:
    """
    Filter out negative numbers and sort the remaining ones in ascending order.
    Suodata negatiiviset luvut ja järjestä jäljelle jääneet nousevaan järjestykseen.

    Args:
        numbers (list): List of integers

    Returns:
        list: Sorted list of positive numbers

    Example:
        >>> filter_and_sort_list([3, -1, 4, -5, 2, -2])
        [2, 3, 4]
    """
    pass


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries. If a key exists in both dictionaries,
    the value should be the sum if both values are integers,
    or concatenated if both values are strings.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Merged dictionary

    Example:
        >>> merge_dictionaries(
            {'a': 1, 'b': 2, 'c': 'hello'},
            {'b': 3, 'c': ' world', 'd': 4}
        )
        {'a': 1, 'b': 5, 'c': 'hello world', 'd': 4}
    """
    pass


def group_by_type(items: list) -> dict:
    """
    Group items by their data type.

    Args:
        items (list): List of mixed-type items

    Returns:
        dict: Dictionary with types as keys and lists of items as values

    Example:
        >>> group_by_type([1, 'hello', 3.14, 'world', 42, 2.71])
        {
            'int': [1, 42],
            'str': ['hello', 'world'],
            'float': [3.14, 2.71]
        }
    """
    pass


def rotate_matrix(matrix: list) -> list:
    """
    Rotate a matrix 90 degrees clockwise.
    Matrix is represented as a list of lists.

    Args:
        matrix (list): Square matrix (n x n)

    Returns:
        list: Rotated matrix

    Example:
        >>> rotate_matrix([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
    """
    pass