#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class PageHeader(SeleniumWrapper):
    FIND_WORKSHOP = (By.CLASS_NAME, "find-a-meeting")

    logger = logging.getLogger("pageheader")

    def __init__(self, driver):
        super().__init__(driver)

    def clickFindWorkshop(self):
        self.clickElement(self.FIND_WORKSHOP)
