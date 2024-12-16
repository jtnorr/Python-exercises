import csv
import os
import unittest

from exercises.file_handling.file_handling_exercises import (
    read_and_count_words,
    process_csv_data,
    save_filtered_data,
    analyze_log_file
)


class TestFileHandling(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test files
        with open('test_text.txt', 'w') as f:
            f.write('Hello World\nHello Python\nPython is great')

        with open('test_grades.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([
                ['student_id', 'subject', 'grade'],
                ['S001', 'Math', '85'],
                ['S001', 'Physics', '86'],
                ['S002', 'Math', '92'],
                ['S002', 'Physics', '92']
            ])

        with open('test_numbers.txt', 'w') as f:
            f.write('1.5\n4.5\n6.7\n2.3\n8.9')

    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        test_files = ['test_text.txt', 'test_grades.csv', 'test_numbers.txt', 'test_output.txt']
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)

    def test_read_and_count_words(self):
        result = read_and_count_words('test_text.txt')
        self.assertEqual(result['hello'], 2)
        self.assertEqual(result['python'], 2)
        self.assertEqual(result['world'], 1)
        with self.assertRaises(FileNotFoundError):
            read_and_count_words('nonexistent.txt')

    def test_process_csv_data(self):
        result = process_csv_data('test_grades.csv')
        self.assertEqual(result['S001'], 85.5)
        self.assertEqual(result['S002'], 92.0)

    def test_save_filtered_data(self):
        count = save_filtered_data('test_numbers.txt', 'test_output.txt', 5.0)
        self.assertEqual(count, 2)
        with open('test_output.txt', 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 2)
            self.assertTrue(all(float(x) >= 5.0 for x in lines))

    def test_analyze_log_file(self):
        # Create a temporary log file
        with open('test_log.txt', 'w') as f:
            f.write('2024-01-01,ERROR,Database failed\n')
            f.write('2024-01-01,WARNING,Disk space low\n')
            f.write('2024-01-02,ERROR,Network down\n')
            f.write('2024-01-02,ERROR,Database failed\n')
            f.write('2024-01-03,WARNING,High CPU usage\n')

        # Test the function
        result = analyze_log_file('test_log.txt')

        # Check the result
        self.assertEqual(result['ERROR'], 3)
        self.assertEqual(result['WARNING'], 2)
        self.assertEqual(result['INFO'], 0)