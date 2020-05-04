
import unittest
from csv_merger import csv_merger

###########################    ###########################    ###############################

### Unit Test Cases for csv_merger.py ###

###########################    ###########################    ###############################

class TestClass(unittest.TestCase):
    def test_file_path_empty(self):
        self.assertEqual(csv_merger.merge_rows(""), "error: no files given")

    def test_file_path_invalid(self):
        path = ("invalid_path")
        self.assertEqual(csv_merger.merge_rows(path), "error: File path is invalid")

    def test_file_empty_header(self):
        self.assertEqual(csv_merger.has_headers(""), "error: File is of invalid format")

    def test_file_invalid_reader(self):
        self.assertEqual(csv_merger.has_headers(""), "error: File is of invalid format")

    def test_file_null_reader(self):
        self.assertEqual(csv_merger.has_headers(None), "reader object has null value")


if __name__ == '__main__':
    unittest.main()



