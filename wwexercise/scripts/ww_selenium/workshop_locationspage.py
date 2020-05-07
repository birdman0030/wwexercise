#!/usr/bin/env python

from .workshop_searchpage import WorkshopSearchPage
from selenium.webdriver.common.by import By


class WorkshopLocationsPage(WorkshopSearchPage):
    # Constants
    AVAILABLE_WORKSHOPS = (By.CLASS_NAME, "meeting-location__top")
    WORKSHOP_DISTANCE = (By.CLASS_NAME, "location__distance")
    WORKSHOP_NAME = (By.CLASS_NAME, "location__name")

    def __init__(self, driver):
        super().__init__(driver)

    def getWorkshopByDistance(self, index: int):
        elements = self.getElements(self.WORKSHOP_NAME)
        return (elements[index].text)

    def clickWorkshopByDistance(self, index: int):
        elements = self.getElements(self.AVAILABLE_WORKSHOPS)
        self.clickElement(elements[index])

    def findDistanceToWorkshop(self, index: int):
        elements = self.getElements(self.WORKSHOP_DISTANCE)
        return (elements[index].text)