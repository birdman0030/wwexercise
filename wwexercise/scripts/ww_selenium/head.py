#!/usr/bin/env python

from .seleniumwrapper import SeleniumWrapper


class Head(SeleniumWrapper):
    """
    Parses web page title using Selenium driver.title method

    :return title: element text for webpage title.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def getHeaderTitleText(self):
        title = self.driver.title
        return title
