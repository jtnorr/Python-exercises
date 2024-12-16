"""
Assignment: Text Analysis Tool

Your task is to create a set of functions that analyze text data. These functions will help you
practice working with strings, lists, loops, and basic algorithms.

Instructions:
1. Complete each function according to its docstring description
2. Run the tests to check your implementation
3. Don't modify the test functions or docstrings

Topics covered:
- String manipulation
- List operations
- Loops and conditionals
- Function parameters and return values

Tehtävä: Tekstianalyysityökalu

Tehtävänäsi on luoda joukko funktioita, jotka analysoivat tekstidataa. Nämä funktiot auttavat sinua
harjoittelemaan merkkijonojen, listojen, silmukoiden ja perusalgoritmien käsittelyä.

Ohjeet:
1. Täydennä jokainen funktio sen docstring-kuvausta vastaavasti
2. Suorita testit tarkistaaksesi toteutuksesi
3. Älä muokkaa testifunktioita tai docstring-kuvausta

Käsitellyt aiheet:
- Merkkijonojen käsittely
- Listojen operaatiot
- Silmukat ja ehdot
- Funktioiden parametrit ja paluuarvot

"""

def count_words(text: str) -> int:
    """
    Count the number of words in a text.
    Words are separated by spaces.
    Empty string should return 0.

    Laske sanojen määrä tekstissä.
    Sanat erotetaan välilyönneillä.
    Tyhjä merkkijono palauttaa 0.

    Args:
        text (str): The input text

    Returns:
        int: Number of words in the text

    Example:
        >>> count_words("Hello world")
        2
        >>> count_words("")
        0
    """
    pass

def find_longest_word(text: str) -> str:
    """
    Find the longest word in the text.
    If there are multiple words of the same length, return the first one.
    If the text is empty, return an empty string.

    Etsi pisin sana tekstissä.
    Jos useita sanoja on samanpituisia, palauta ensimmäinen.
    Jos teksti on tyhjä, palauta tyhjä merkkijono.

    Args:
        text (str): The input text

    Returns:
        str: The longest word found

    Example:
        >>> find_longest_word("The quick brown fox")
        "quick"
        >>> find_longest_word("")
        ""
    """
    pass

def count_vowels(text: str) -> dict:
    """
    Count the occurrence of each vowel (a, e, i, o, u) in the text.
    The count should be case-insensitive.

    Laske jokaisen vokaalin (a, e, i, o, u) esiintymiskerrat tekstissä.
    Laskenta ei huomioi kirjainkoosta

    Args:
        text (str): The input text

    Returns:
        dict: Dictionary with vowels as keys and their count as values

    Example:
        >>> count_vowels("Hello World")
        {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
    """
    pass

def is_palindrome(text: str) -> bool:
    """
    Check if the text is a palindrome.
    A palindrome reads the same forwards and backwards, ignoring spaces and case.

    Tarkista, onko teksti palindromi.
    Palindromi on sana tai lause, joka luetaan samalla tavalla eteen- ja taaksepäin, huomioiden vain kirjaimet.

    Args:
        text (str): The input text

    Returns:
        bool: True if text is a palindrome, False otherwise

    Example:
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    pass
