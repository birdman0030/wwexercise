#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class FindWorkshopPage(SeleniumWrapper):
    # Constants
    INPUT_FIND_WORKSHOP = (By.ID, "meetingSearch")
    AVAILABLE_WORKSHOPS = (By.CLASS_NAME, "meeting-location__top")
    WORKSHOP_DISTANCE = (By.CLASS_NAME, "location__distance")
    WORKSHOP_NAME = (By.CLASS_NAME, "location__name")
    WORKSHOP_DAY_SCHEDULE = (By.CLASS_NAME, "schedule-detailed-day")
    WORKSHOP_DAY = (By.CLASS_NAME, "schedule-detailed-day-label")
    WORKSHOP = (By.CLASS_NAME, "schedule-detailed-day-meetings-item")
    WORKSHOP_LEADER = (By.CLASS_NAME, "schedule-detailed-day-meetings-item-leader")
    WORKSHOP_TIME = (By.CLASS_NAME, "schedule-detailed-day-meetings-item-time")

    logger = logging.getLogger("findworkshop_page")

    def __init__(self, driver):
        super().__init__(driver)

    def typeZipCode(self, text: str):
        self.typeInElement(self.INPUT_FIND_WORKSHOP, text)
        self.pressEnter(self.INPUT_FIND_WORKSHOP)

# ---split---

    def getWorkshopByDistance(self, index: int):
        elements = self.getElements(self.WORKSHOP_NAME)
        return (elements[index].text)

    def clickWorkshopByDistance(self, index: int):
        elements = self.getElements(self.AVAILABLE_WORKSHOPS)
        self.clickElement(elements[index])

    def findDistanceToWorkshop(self, index: int):
        elements = self.getElements(self.WORKSHOP_DISTANCE)
        return (elements[index].text)

# ---split---

    def getActiveWorkshopName(self):
        return self.getElementText(self.WORKSHOP_NAME)

    def findWorkshopScheduleByDay(self, day: str):
        elements = self.getElements(self.WORKSHOP_DAY_SCHEDULE)
        for element in elements:
            if element.find_element(*self.WORKSHOP_DAY).text == day.upper():
                return element
        print(f"NO {day} found")
        #raise ValueError(f"Invalid parameter: {day}")

    def getLeaderWorkshopNumByDay(self, day: str):
        schedule = {}
        leaders = []
        schedule_element = self.findWorkshopScheduleByDay(day)
        leader_elements = schedule_element.find_elements(*self.WORKSHOP_LEADER)
        for leader_element in leader_elements:
            leaders.append(leader_element.text)
        for i in leaders:
            schedule[i] = schedule.get(i, 0) + 1
        return schedule

    def printDailySchedule(self, day: str):
        content = self.getLeaderWorkshopNumByDay(day)
        for key, val in content.items():
            self.logger.info(f"{key} {val}")
