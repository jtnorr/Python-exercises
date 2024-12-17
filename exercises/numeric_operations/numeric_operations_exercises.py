"""
Exercise: Basic Numeric Operations and Control Flow

This exercise focuses on:
- Working with numbers
- Conditional statements
- Loops
- Basic algorithms

Tehtävä: Perusnumeeriset operaatiot ja ohjausrakenteet

Tämä tehtävä keskittyy:
- Numeroiden käsittelyyn
- Ehtolauseisiin
- Silmukoihin
- Perusalgoritmeihin
"""

def calculate_series_sum(n: int) -> int:
    """
    Calculate the sum of the series: 1 + 2 + 3 + ... + n

    Laske sarjan summa: 1 + 2 + 3 + ... + n

    Args:
        n (int): The last number in the series (n > 0)

    Returns:
        int: The sum of the series

    Raises:
        ValueError: If n is less than or equal to 0

    Example:
        >>> calculate_series_sum(5)
        15  # Because 1 + 2 + 3 + 4 + 5 = 15
    """
    pass

def is_prime(number: int) -> bool:
    """
    Check if a number is prime.
    A prime number is only divisible by 1 and itself.

    Tarkista, onko luku alkuluku.
    Alkuluku on jaollinen vain yhdellä ja itsellään.

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
    """
    pass

def get_fibonacci_sequence(n: int) -> list:
    """
    Generate Fibonacci sequence up to n terms.
    Fibonacci sequence: each number is the sum of the two preceding ones.

    Generoi Fibonaccin lukujono n ensimmäistä termiä.
    Fibonaccin lukujono: jokainen luku on kahden edellisen luvun summa.

    Args:
        n (int): Number of terms to generate (n > 0)

    Returns:
        list: List containing the Fibonacci sequence

    Example:
        >>> get_fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
    """
    pass

def multiply_table(n: int) -> list:
    """
    Generate a multiplication table up to n.

    Generoi kertotaulu n asti.

    Args:
        n (int): The size of the multiplication table (n > 0)

    Returns:
        list: A 2D list representing the multiplication table

    Example:
        >>> multiply_table(3)
        [[1, 2, 3],
         [2, 4, 6],
         [3, 6, 9]]
    """
    pass
