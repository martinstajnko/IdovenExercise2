""" This module contains all the locators of the page. """
from selenium.webdriver.common.by import By

MAIN_TITLE = (By.XPATH, "//h1[text()='Free Website Speed Test']")
INPUT_FIELD = (By.CSS_SELECTOR, "input[name='url']")
BUTTON_START_TEST = (By.CSS_SELECTOR, "button[type='submit']")

WAITING_BAR = (By.XPATH, "//div[@class='d-flex ']//div[1]")
WAITING_PROCESS = (By.XPATH, "//div[text()='{url}']")
METRIC_OVERVIEW = (By.ID, 'metric-overview')

EMPTY_FIELD = (By.XPATH, "//div[text()='Enter a website URL to start the performance test']")


RESULT_ELEMENTS = [
    (By.XPATH, "//span[@title='Full TTFB']"),
    (By.XPATH, "//span[@title='First Contentful Paint']"),
    (By.XPATH, "//span[@title='Largest Contentful Paint']"),
    (By.XPATH, "//span[@title='Speed Index']"),
    (By.XPATH, "//span[@title='CPU Time']"),
    (By.XPATH, "//span[@title='Total Blocking Time']"),
    (By.XPATH, "//span[@title='Cumulative Layout Shift']"),
    (By.XPATH, "//span[@title='Page Weight']")
]
