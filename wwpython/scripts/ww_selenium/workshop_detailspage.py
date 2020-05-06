#!/usr/bin/env python

import logging
from .workshop_locationspage import WorkshopLocationsPage
from selenium.webdriver.common.by import By


class WorkshopDetailsPage(WorkshopLocationsPage):
    # Constants
    WORKSHOP_DAY_SCHEDULE = (By.CLASS_NAME, "schedule-detailed-day")
    WORKSHOP_DAY = (By.CLASS_NAME, "schedule-detailed-day-label")
    WORKSHOP_LEADER = (By.CLASS_NAME, "schedule-detailed-day-meetings-item-leader")
    LOGGER = logging.getLogger("workshop_detailspage")

    def __init__(self, driver):
        super().__init__(driver)

    def getActiveWorkshopName(self):
        return self.getElementText(self.WORKSHOP_NAME)

    def findWorkshopScheduleByDay(self, day: str):
        elements = self.getElements(self.WORKSHOP_DAY_SCHEDULE)
        for element in elements:
            if element.find_element(*self.WORKSHOP_DAY).text == day.upper():
                return element
        raise ValueError(f"Invalid parameter: {day}")

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
            self.LOGGER.info(f"{key} {val}")
