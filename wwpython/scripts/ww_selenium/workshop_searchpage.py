#!/usr/bin/env python

from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class WorkshopSearchPage(SeleniumWrapper):
    # Constants
    INPUT_FIND_WORKSHOP = (By.ID, "meetingSearch")

    def __init__(self, driver):
        super().__init__(driver)

    def typeZipCode(self, text: str):
        self.typeInElement(self.INPUT_FIND_WORKSHOP, text)
        self.pressEnter(self.INPUT_FIND_WORKSHOP)
