#!/usr/bin/env python

from .seleniumwrapper import SeleniumWrapper


class Head(SeleniumWrapper):

    def __init__(self, driver):
        super().__init__(driver)

    def getHeaderTitleText(self):
        title = self.driver.title
        return title
