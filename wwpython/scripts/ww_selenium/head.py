#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class Head(SeleniumWrapper):
    logger = logging.getLogger("head")

    def __init__(self, driver):
        super().__init__(driver)

    def getHeaderTitleText(self):
        title = self.driver.title
        return title
