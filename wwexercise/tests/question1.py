import logging
import unittest
import sys
import os

from wwexercise.scripts.parser.parser import Parser

# Setup unittest logging
LOGGER = logging.getLogger()
LOGGER.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
LOGGER.addHandler(stream_handler)


class WWNavigation(unittest.TestCase):
    # Constants
    VALID_PATH = os.path.join("wwexercise", "data", "sample_data.txt")
    INVALID_PATH = os.path.join("This_File_Does_Not_Exist.json")
    LOGGER = logging.getLogger(__name__)

    @classmethod
    def setUpClass(self):
        self.LOGGER.info("### QUESTION 1 ###")

    def test_question1_valid_path(self):
        # Test valid path returns True
        self.LOGGER.info("\n### Test Run: Valid Path ###")
        parser = Parser(self.VALID_PATH)
        self.LOGGER.info(f"File Path = {self.VALID_PATH}")
        self.assertTrue(parser.doesFileExist(), f"{self.VALID_PATH} file does not exist")
        self.LOGGER.info("Valid path returned 'True'")

        # Test invalid path throws IOERROR exception
        self.LOGGER.info("\n### Test Run: Invalid Path ###")
        parser = Parser(self.INVALID_PATH)
        self.LOGGER.info(f"File Path = {self.INVALID_PATH}")
        with self.assertRaises(IOError):
            parser.doesFileExist()
        self.LOGGER.info("Invalid path threw IOERROR exception")

        # Parse file
        self.LOGGER.info("\n### Test Run: Parse File ###")
        parser = Parser(self.VALID_PATH)
        results = parser.parseFile()
        parser.printResults(results)

    @classmethod
    def tearDownClass(self):
        self.LOGGER.removeHandler(stream_handler)


if __name__ == '__main__':
    unittest.main()
