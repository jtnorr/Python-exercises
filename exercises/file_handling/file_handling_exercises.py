"""
Assignment: File Handling and Data Processing

This assignment focuses on:
- Reading and writing files
- Processing CSV data
- Error handling
- Data analysis

Tehtävä: Tiedostojen käsittely ja datan prosessointi

Tämä tehtävä keskittyy:
- Tiedostojen lukemiseen ja kirjoittamiseen
- CSV-datan käsittelyyn
- Virheiden käsittelyyn
- Datan analysointiin

"""

def read_and_count_words(filename: str) -> dict:
    """
    Read a text file and count word frequencies.
    Words should be converted to lowercase and stripped of punctuation.

    Lue tekstitiedosto ja laske sanojen esiintyvyys.
    Sanat tulisi muuntaa pieniksi kirjaimiksi ja poistaa välimerkit.

    Args:
        filename (str): Path to the text file

    Returns:
        dict: Dictionary with words as keys and their frequencies as values

    Raises:
        FileNotFoundError: If the file doesn't exist

    Example:
        >>> read_and_count_words('sample.txt')
        {'hello': 2, 'world': 1, 'python': 3}
    """
    pass

def process_csv_data(filename: str) -> dict:
    """
    Process a CSV file containing student grades.
    CSV format: student_id,subject,grade

    Käsittele opiskelijoiden arvosanoja sisältävä CSV-tiedosto.
    CSV-muoto: student_id,subject,grade

    Args:
        filename (str): Path to the CSV file

    Returns:
        dict: Dictionary with student IDs as keys and their average grades as values

    Example:
        >>> process_csv_data('grades.csv')
        {'S001': 85.5, 'S002': 92.0}
    """
    pass

def save_filtered_data(input_file: str, output_file: str, min_value: float) -> int:
    """
    Read numbers from input file, filter out values below min_value,
    and save remaining numbers to output file.

    Lue luvut syötetiedostosta, suodata arvot, jotka ovat pienempiä kuin min_value,
    ja tallenna jäljelle jääneet luvut tulostetiedostoon.

    Args:
        input_file (str): Path to input file (one number per line)
        output_file (str): Path to output file
        min_value (float): Minimum value to include

    Returns:
        int: Number of values written to output file

    Example:
        >>> save_filtered_data('input.txt', 'output.txt', 5.0)
        3  # Number of values written
    """
    pass

def analyze_log_file(filename: str) -> dict:
    """
    Analyze a log file and extract statistics.
    Log format: timestamp,level,message

    Analysoi lokitiedosto ja kerää tilastoja.
    Lokin muoto: aikaleima,taso,viesti

    Args:
        filename (str): Path to log file

    Returns:
        dict: Dictionary containing:
            - 'error_count': number of ERROR messages
            - 'warning_count': number of WARNING messages
            - 'info_count': number of INFO messages
            - 'most_common_error': most frequent error message

    Example:
        >>> analyze_log_file('app.log')
        {
            'error_count': 5,
            'warning_count': 10,
            'info_count': 15,
            'most_common_error': 'Database connection failed'
        }
    """
    pass
