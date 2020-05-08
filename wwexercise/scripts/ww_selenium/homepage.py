#!/usr/bin/env python

from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class HomePage(SeleniumWrapper):
    """
    Weight Watchers(US) homepage
    """
    # Constants
    # CSS Selector by Attribute=Value is used due to code readability.
    FIND_WORKSHOP = (By.CSS_SELECTOR, '[da-action="nav_header_find-a-workshop"]')

    def __init__(self, driver):
        super().__init__(driver)

    def clickFindWorkshop(self):
        """
        Clicks the 'Find a Workshop' button on the weight watchers home page.
        """
        self.clickElement(self.FIND_WORKSHOP)
