import logging
import unittest
import os
import sys

from configuration import ROOT_DIR
from wwexercise.scripts.ww_selenium.homepage import HomePage
from wwexercise.scripts.ww_selenium.workshop_searchpage import WorkshopSearchPage
from wwexercise.scripts.ww_selenium.workshop_locationspage import WorkshopLocationsPage
from wwexercise.scripts.ww_selenium.workshop_detailspage import WorkshopDetailsPage
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Setup unittest logging
LOGGER = logging.getLogger()
LOGGER.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
LOGGER.addHandler(stream_handler)


class WWNavigation(unittest.TestCase):
    HOMEPAGE_TITLE = "WW (Weight Watchers): Weight Loss & Wellness Help"
    FIND_WORKSHOP_TITLE = "Find WW Studios & Meetings Near You | WW USA"
    LOGGER = logging.getLogger(__name__)

    def setUp(self):
        self.LOGGER.info("### Test Run: Question 2 ###\n")
        self.errors = []
        # create a new session with chrome options
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('log-level=OFF')
        options.add_experimental_option('excludeSwitches',
                                        ['enable-logging'])
        driver_path = os.path.join(ROOT_DIR,
                                   "wwexercise",
                                   "drivers",
                                   "chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=driver_path,
                                       options=options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # Instantiate web page classes.
        self.home = HomePage(self.driver)
        self.find_workshop = WorkshopSearchPage(self.driver)
        self.details_workshop = WorkshopDetailsPage(self.driver)
        self.locations_workshop = WorkshopLocationsPage(self.driver)

    def test_question2(self):
        # Navigate to the home page
        self.driver.get("https://www.weightwatchers.com/us/")

        # Verify homepage title
        current_title = self.driver.title

        # If page title != HOMEPAGE_TITLE,
        # catch Assertion error and continue.
        try:
            self.assertEqual(current_title, self.HOMEPAGE_TITLE)
            self.LOGGER.info("Current title matches expected title")
        except AssertionError as e:
            self.errors.append(str(e))

        # Verify Find a Workshop title
        self.home.clickFindWorkshop()
        current_title = self.driver.title

        # If page title != FIND_WORKSHOP_TITLE,
        # catch Assertion error and continue.
        try:
            self.assertIn(self.FIND_WORKSHOP_TITLE, current_title)
            self.LOGGER.info("Current title contains expected title")
        except AssertionError as e:
            self.errors.append(str(e))

        # Find workshop by ZipCode and search.
        self.find_workshop.typeZipCode("10011")

        # Find the nearest workshop and distance.
        nearest_workshop = self.locations_workshop.getWorkshopByDistance(0)
        distance = self.locations_workshop.findDistanceToWorkshop(0)
        self.LOGGER.info(f"{nearest_workshop} = {distance}")

        # Click on the nearest workshop.
        self.locations_workshop.clickWorkshopByDistance(0)

        # Verify displayed location name matches
        # the name of the first searched result
        active_workshop = self.details_workshop.getActiveWorkshopName()

        # If selected workshop name != searched workshop name,
        # catch Assertion error and continue.
        try:
            self.assertEqual(nearest_workshop, active_workshop)
            self.LOGGER.info("Selected workshop matches searched location")
        except AssertionError as e:
            self.errors.append(str(e))

        # Find daily workshop leaders shift count and log to console
        self.details_workshop.printDailySchedule("Sun")

    def tearDown(self):
        # Close the browser
        self.driver.close()

        # If errors were found, log them to screen and fail test.
        if self.errors:
            self.LOGGER.info('\n-----ERRORS-----')
            for error in self.errors:
                self.LOGGER.error(error)
            raise Exception(f"{len(self.errors)} Error(s) found")

        # Remove logging stream handler
        self.LOGGER.removeHandler(stream_handler)


if __name__ == '__main__':
    unittest.main()
