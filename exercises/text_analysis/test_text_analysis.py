"""
Test cases for text_analysis_exercises.py
"""

import unittest
from exercises.text_analysis.text_analysis_exercises import (
    count_words,
    find_longest_word,
    count_vowels,
    is_palindrome
)

class TestTextAnalysis(unittest.TestCase):
    """Unit tests for text analysis exercises"""

    def test_count_words(self):
        """Test count_words function"""
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("One"), 1)
        self.assertEqual(count_words("   Multiple   Spaces   Between   "), 3)

    def test_find_longest_word(self):
        """Test find_longest_word function"""
        self.assertEqual(find_longest_word("The quick brown fox"), "quick")
        self.assertEqual(find_longest_word(""), "")
        self.assertEqual(find_longest_word("Short and longer words"), "longer")
        self.assertEqual(find_longest_word("Same same"), "same")

    def test_count_vowels(self):
        """Test count_vowels function"""
        self.assertEqual(
            count_vowels("Hello World"),
            {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
        )
        self.assertEqual(
            count_vowels("AEIOU"),
            {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        )
        self.assertEqual(
            count_vowels(""),
            {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        )

    def test_is_palindrome(self):
        """Test is_palindrome function"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("race car"))
        self.assertFalse(is_palindrome("hello world"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
