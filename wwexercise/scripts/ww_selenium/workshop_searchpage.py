#!/usr/bin/env python

from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class WorkshopSearchPage(SeleniumWrapper):
    """
    Weight Watchers(US) search for nearby workshops page
    """
    # Constants
    INPUT_FIND_WORKSHOP = (By.ID, "meetingSearch")

    def __init__(self, driver):
        super().__init__(driver)

    def typeZipCode(self, text: str):
        """
        Enters zipcode in search box to find nearby workshops. Sends Enter key
        to initiate search.

        :param text: string of keys to enter.
        """
        self.typeInElement(self.INPUT_FIND_WORKSHOP, text)
        self.pressEnter(self.INPUT_FIND_WORKSHOP)
