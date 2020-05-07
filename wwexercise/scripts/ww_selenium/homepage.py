#!/usr/bin/env python

from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class HomePage(SeleniumWrapper):
    # Constants

    # CSS Selector by Attribute is used due to issues in HTML and code
    # readability. In homepage.py because Element consistent between pages.
    FIND_WORKSHOP = (By.CSS_SELECTOR, '[da-action="nav_header_find-a-workshop"]')

    def __init__(self, driver):
        super().__init__(driver)

    def clickFindWorkshop(self):
        self.clickElement(self.FIND_WORKSHOP)
