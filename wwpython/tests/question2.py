import logging
import unittest
import os
import sys

from configuration import ROOT_DIR
from wwpython.scripts.ww_selenium.head import Head
from wwpython.scripts.ww_selenium.pageheader import PageHeader
from wwpython.scripts.ww_selenium.homepage import HomePage
from wwpython.scripts.ww_selenium.FindWorkshopPage import FindWorkshopPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


logger = logging.getLogger()
logger.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class WWNavigation(unittest.TestCase):
    HOMEPAGE_TITLE = "WW (Weight Watchers): Weight Loss & Wellness Help | WW USA"
    FIND_WORKSHOP_TITLE = "Find WW Studios & Meetings Near You | WW USA"

    logger = logging.getLogger(__name__)

    def test_question_2(self):
        # create a new session
        errors = []
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('log-level=OFF')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver_path = os.path.join(ROOT_DIR,
                                   "wwpython",
                                   "drivers",
                                   "chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.navbar = PageHeader(self.driver)
        self.find_workshop = FindWorkshopPage(self.driver)
        self.driver.get("https://www.weightwatchers.com/us/")

        # Verify homepage title
        current_title = self.driver.title
        if current_title != self.HOMEPAGE_TITLE:
            logger.info(f"{current_title} != {self.HOMEPAGE_TITLE}")
            errors.append(f"{current_title} != {self.HOMEPAGE_TITLE}")
        else:
            logger.info(f"{current_title} = {self.HOMEPAGE_TITLE}")

        # Click Find a Workshop
        self.navbar.clickFindWorkshop()
        current_title = self.driver.title
        if current_title != self.FIND_WORKSHOP_TITLE:
            logger.info(f"{current_title} != {self.FIND_WORKSHOP_TITLE}")
            errors.append(f"{current_title} != {self.FIND_WORKSHOP_TITLE}")
        else:
            logger.info(f"{current_title} = {self.FIND_WORKSHOP_TITLE}")

        # Find workshop by ZipCode
        self.find_workshop.typeZipCode("10011")
        nearest_workshop = self.find_workshop.getWorkshopByDistance(0)
        distance = self.find_workshop.findDistanceToWorkshop(0)
        logger.info(f"{nearest_workshop} = {distance}")
        self.find_workshop.clickWorkshopByDistance(0)
        active_workshop = self.find_workshop.getActiveWorkshopName()


        #self.assertEqual(nearest_workshop,
        #                 active_workshop,
        #                 "Searched workshop name does not "
        #                 "match active workshop name"
        #                 )

# --- New Test: Get the workshop times ... hours of operation do not exist...covid update?

    #def test_get_leader_daily_workshop_count(self):
        self.find_workshop.printDailySchedule("Sun")

    def tearDown(self):
        logger.removeHandler(stream_handler)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
