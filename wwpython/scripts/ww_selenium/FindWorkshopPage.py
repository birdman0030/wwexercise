#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class FindWorkshopPage(SeleniumWrapper):
    INPUT_FIND_WORKSHOP = (By.ID, "meetingSearch")
    AVAILABLE_WORKSHOPS = (By.CLASS_NAME, "meeting-location")
    WORKSHOP_DISTANCE = (By.CLASS_NAME, "location__distance")
    WORKSHOP_DAY_SCHEDULE = (By.CLASS_NAME, ".schedule-detailed-day-label")

    logger = logging.getLogger("findworkshoppage")

    def __init__(self, driver):
        super().__init__(driver)

    def clickFindWorkshop(self, text: str):
        self.typeInElement(self.INPUT_FIND_WORKSHOP, text)
        self.pressEnter(self.INPUT_FIND_WORKSHOP)

    def findWorkshopByDistance(self, index):
        elements = self.getElements(self.AVAILABLE_WORKSHOPS)
        return elements[index]

    def findWorkshopDistance(self, parent_element):
        element = parent_element.find_element(self.WORKSHOP_DISTANCE)
        return self.getElementText(element)

    def getWorkshopDailySchedule(self, day: str):
        elements = self.getElements(self.WORKSHOP_DAY_SCHEDULE)
        for element in elements:
            if self.getElementText(element) == day:
                #retrieve the daily schedule
                print("TBD")

