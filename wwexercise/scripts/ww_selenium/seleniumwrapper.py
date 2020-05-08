#!/usr/bin/env python

import logging
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementNotInteractableException,
    InvalidElementStateException
)


class SeleniumWrapper(object):
    """
    Wraps Selenium methods
    """

    def __init__(self, driver):
        """
        Initialize driver and logging for Selenium Wrapper.

        :param driver: Webdriver object instance
        """
        self.driver = driver
        self.logger = logging.getLogger('seleniumwrapper')

    def _getElement(self, element):
        """
        Finds a web element on a web page.

        :param element: Element object or tuple (By.selector, identifier)
        :return Web element object.
        """
        if isinstance(element, WebElement):
            return element
        elif isinstance(element, tuple):
            return self.driver.find_element(*element)
        else:
            raise TypeError(f"Unable to find element given a {type(element)}"
                            f" equal to {element}")

    def getElements(self, element):
        """
        Finds all web elements on a web page.

        :param element: Element object or tuple (By.selector, identifier)
        :return a list of web element objects.
        """
        if isinstance(element, WebElement):
            return element
        if isinstance(element, tuple):
            return self.driver.find_elements(*element)
        else:
            raise TypeError(f"Unable to find elements given a {type(element)}"
                            f" equal to {element}")

    def clickElement(self, element):
        """
        Finds an element and clicks on it.

        :param element: Element object or tuple (By.selector, identifier)
        """
        element = self._getElement(element)
        element.click()

    def getElementText(self, element):
        """
        Finds an element and returns the element text.

        :param element: Element object or tuple (By.selector, identifier)
        :return string of the element text.
        """
        element = self._getElement(element)
        return element.text

    def typeInElement(self, element, txt, clear_txt=True):
        """
        Finds an element for a text box, clears the text (optional), and
        enters keys into text box.

        :param element: Element object or tuple (By.selector, identifier)
        :param txt: string of keys to enter into text box
        :param clear_txt: optional bool to clear text box prior to input.
        """
        element = self._getElement(element)
        try:
            if clear_txt:
                element.clear()
            element.send_keys(txt)
        except InvalidElementStateException as e:
            self.logger.error(f"Unable to edit element {element}")
            raise e

    def pressEnter(self, element):
        """
        Finds a web element text box and sends an enter key.

        :param element: Element object or tuple (By.selector, identifier)
        """
        element = self._getElement(element)
        try:
            element.send_keys(Keys.RETURN)
        except ElementNotInteractableException as e:
            raise e
