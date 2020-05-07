import logging
import unittest
import os
import sys

from configuration import ROOT_DIR
from wwpython.scripts.ww_selenium.homepage import HomePage
from wwpython.scripts.ww_selenium.workshop_searchpage import WorkshopSearchPage
from wwpython.scripts.ww_selenium.workshop_locationspage import WorkshopLocationsPage
from wwpython.scripts.ww_selenium.workshop_detailspage import WorkshopDetailsPage
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
        # create a new session
        self.errors = []
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('log-level=OFF')
        options.add_experimental_option('excludeSwitches',
                                        ['enable-logging'])
        driver_path = os.path.join(ROOT_DIR,
                                   "wwpython",
                                   "drivers",
                                   "chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.home = HomePage(self.driver)
        self.find_workshop = WorkshopSearchPage(self.driver)
        self.details_workshop = WorkshopDetailsPage(self.driver)
        self.locations_workshop = WorkshopLocationsPage(self.driver)

    def test_question2(self):
        # Navigate to the home page
        self.driver.get("https://www.weightwatchers.com/us/")

        # Verify homepage title
        current_title = self.driver.title
        if current_title != self.HOMEPAGE_TITLE:
            LOGGER.info(f"Error: Homepage title does match expected")
            self.errors.append(f"{current_title} != expected title")
        else:
            LOGGER.info(f"HOMEPAGE TITLE MATCHES: {self.HOMEPAGE_TITLE}")

        # Verify Find a Workshop title
        self.home.clickFindWorkshop()
        current_title = self.driver.title
        if current_title != self.FIND_WORKSHOP_TITLE:
            LOGGER.info(f"Error: Find a workshop title does not match expected")
            self.errors.append(f"{current_title} != expected title")
        else:
            LOGGER.info(f"WORKSHOP TITLE MATCHES = {self.FIND_WORKSHOP_TITLE}")

        # Find nearest workshop by ZipCode
        self.find_workshop.typeZipCode("10011")
        nearest_workshop = self.locations_workshop.getWorkshopByDistance(0)
        distance = self.locations_workshop.findDistanceToWorkshop(0)
        LOGGER.info(f"{nearest_workshop} = {distance}")
        self.locations_workshop.clickWorkshopByDistance(0)

        # Verify displayed location name matches the name of the first searched result
        active_workshop = self.details_workshop.getActiveWorkshopName()
        if nearest_workshop != active_workshop:
            LOGGER.info("Selected workshop does not match displayed location")
            self.errors.append(f"{current_title} != Selected WorkShop Name")
        else:
            LOGGER.info(f"SELECTED WORKSHOP NAME MATCHES DISPLAYED NAME")

        # Find daily workshop leaders shift count and log to console
        self.details_workshop.printDailySchedule("Sun")

    def tearDown(self):
        self.driver.close()
        if self.errors:
            LOGGER.info('\n-----ERRORS-----')
            for error in self.errors:
                LOGGER.error(error)
            self.assertEqual(1, 2, "The test failed due to the errors above")
        LOGGER.removeHandler(stream_handler)


if __name__ == '__main__':
    unittest.main()
