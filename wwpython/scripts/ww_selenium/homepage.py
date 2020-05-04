#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By

class HomePage(SeleniumWrapper):
    #CONSTANTS

    logger = logging.getLogger("homepage")

    def __init__(self, driver):
        super()._init_(driver)

# Homepage work TBD