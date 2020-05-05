#!/usr/bin/env python

import logging
from .seleniumwrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class FindWorkshopPage(SeleniumWrapper):
    INPUT_FIND_WORKSHOP = (By.ID, "meetingSearch")
    AVAILABLE_WORKSHOPS = (By.CLASS_NAME, "meeting-location")
    WORKSHOP_DISTANCE = (By.CLASS_NAME, "location__distance")
    WORKSHOP_DAY_SCHEDULE = (By.CLASS_NAME, "schedule-detailed-day")
    WORKSHOP_DAY = (By.CLASS_NAME, "schedule-detailed-day-label")
    WORKSHOP = (By.CLASS_NAME, "schedule-detailed-day-meetings-item")
    WORKSHOP_LEADER = (By.CLASS_NAME, "schedule-detailed-day-meetings-item-leader")
    WORKSHOP_TIME = (By.CLASS_NAME, "schedule-detailed-day-meetings-item-time")

    logger = logging.getLogger("findworkshop_page")

    def __init__(self, driver):
        super().__init__(driver)

    def clickFindWorkshop(self, text: str):
        self.typeInElement(self.INPUT_FIND_WORKSHOP, text)
        self.pressEnter(self.INPUT_FIND_WORKSHOP)

    def findWorkshopByDistance(self, index: int):
        elements = self.getElements(self.AVAILABLE_WORKSHOPS)
        return elements[index]

    def findDistanceToWorkshop(self, parent_element):
        element = parent_element.find_element(self.WORKSHOP_DISTANCE)
        return self.getElementText(element)

    def findWorkshopScheduleByDay(self, day: str):
        elements = self.getElements(self.WORKSHOP_DAY_SCHEDULE)
        for element in elements:
            day_element = element.find_elements(self.WORKSHOP_DAY)
            if day_element.text == day:
                return element
        raise ValueError(f"Invalid parameter: {day}")

    def getLeaderWorkshopNumByDay(self, day: str):
        schedule = {}
        leaders = []
        schedule_element = self.findWorkshopScheduleByDay(day)
        leader_elements = schedule_element.get_elements(self.WORKSHOP_LEADER)
        for leader_element in leader_elements:
            leaders.append(leader_element.text)
        for i in leaders:
            schedule[i] = schedule.get(i, 0) + 1
        return leaders

    def printDailySchedule(self, day: str):
        content = self.getLeaderWorkshopNumByDay(day)
        for key, val in content:
            self.logger.info(f"{key} {val}")
