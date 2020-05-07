import logging
import unittest
import sys

from wwexercise.scripts.number_generator.randnum import (
    randomNumGen, findNumPosition
)

# Setup unittest logging
LOGGER = logging.getLogger()
LOGGER.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
LOGGER.addHandler(stream_handler)


class WWNavigation(unittest.TestCase):
    # Constants
    LOGGER = logging.getLogger(__name__)

    @classmethod
    def setUpClass(self):
        self.LOGGER.info("### QUESTION 3 ###")

    def test_question1_valid_path(self):
        # Test valid path returns True
        self.LOGGER.info("\n### Test Run: Generate Random Numbers ###")
        self.LOGGER.info("Generates a list of 500 random numbers between 0-1000")
        container = randomNumGen()
        self.LOGGER.info(f"{container}")
        self.LOGGER.info("\n### Test Run: find the 10th smallest number")
        self.LOGGER.info(findNumPosition(container, 10))

    @classmethod
    def tearDownClass(self):
        self.LOGGER.removeHandler(stream_handler)


if __name__ == '__main__':
    unittest.main()
