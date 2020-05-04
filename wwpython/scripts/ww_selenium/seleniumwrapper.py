#!/usr/bin/env python

import logging

# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import(
    ElementNotInteractableException,
    InvalidElementStateException
)


class SeleniumWrapper(object):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('seleniumwrapper')

    def _getElement(self, element):
        if isinstance(element, tuple):
            return self.driver.find_element(*element)
        else:
            raise TypeError(f"Unable to find element given a {type(element)}"
                            f" equal to {element}")

    def getElements(self, element):
        if isinstance(element, tuple):
            return self.driver.find_elements(*element)
        else:
            raise TypeError(f"Unable to find elements given a {type(element)}"
                            f" equal to {element}")

    def clickElement(self, element):
        element = self._getElement(element)
        element.click()

    def getElementText(self, element):
        element = self._getElement(element)
        return element.text

    def typeInElement(self, element, txt, clear_txt=True):
        element = self._getElement(element)
        try:
            if clear_txt:
                element.clear()
            element.send_keys(txt)
        except InvalidElementStateException as e:
            self.logger.error(f"Unable to edit element {element}")
            raise e

    def pressEnter(self, element):
        element = self._getElement(element)
        try:
            element.send_keys(Keys.RETURN)
        except ElementNotInteractableException as e:
            raise e
