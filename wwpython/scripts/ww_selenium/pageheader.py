#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class PageHeader(SeleniumWrapper):
    FIND_WORKSHOP = (By.CSS_SELECTOR, '[da-action="nav_header_find-a-workshop"]')

    logger = logging.getLogger("pageheader")

    def __init__(self, driver):
        super().__init__(driver)

    def clickFindWorkshop(self):
        self.clickElement(self.FIND_WORKSHOP)
