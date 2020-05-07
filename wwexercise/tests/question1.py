import logging
import unittest
import sys
import os

from wwpython.scripts.parser.parser import Parser

# Setup unittest logging
LOGGER = logging.getLogger()
LOGGER.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
LOGGER.addHandler(stream_handler)


class WWNavigation(unittest.TestCase):
    # Constants
    VALID_PATH = os.path.join("wwpython", "data", "sample_data.txt")
    INVALID_PATH = os.path.join("This_File_Does_Not_Exist.json")
    LOGGER = logging.getLogger(__name__)

    def test_question1_valid_path(self):
        self.LOGGER.info("\n### Test Run: Valid Path - Question 1 ###")
        parser = Parser(self.VALID_PATH)
        self.LOGGER.info(f"File Path = {self.VALID_PATH}")
        self.assertTrue(parser.doesFileExist(), f"{self.VALID_PATH} file does not exist")

    def test_question1_invalid_path(self):
        self.LOGGER.info("\n### Test Run: Invalid Path - Question 1 ###")
        parser = Parser(self.INVALID_PATH)
        self.LOGGER.info(f"File Path = {self.INVALID_PATH}")
        with self.assertRaises(IOError):
            parser.doesFileExist()

    def test_question1_parse_file(self):
        self.LOGGER.info("\n### Test Run: Parse File - Question 1 ###")
        parser = Parser(self.VALID_PATH)
        self.LOGGER.info(f"File Path = {self.VALID_PATH}")
        results = parser.parseFile()
        parser.printResults(results)


if __name__ == '__main__':
    unittest.main()
