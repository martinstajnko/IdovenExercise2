""" This module contains functions for interacting with the page. """
from urllib.parse import urlparse

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from qaa.page_object import locator


def get_netloc_from_url(url: str) -> str:
    parsed_url = urlparse(url)
    return parsed_url.netloc

def open_page(driver: WebDriver, url: str) -> None:
    driver.get(url)
        

def wait_for_page_to_load(driver: WebDriver, locator: tuple) -> None:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((locator)))

        
def get_element(driver: WebDriver, locator: tuple) -> str:
    return driver.find_element(*locator)

def get_waiting_process_text(driver: WebDriver, url: str) -> str:
    return driver.find_element(locator.WAITING_PROCESS[0], locator.WAITING_PROCESS[1].replace('{url}', url)).text


def input_field(driver: WebDriver, url: str, lacator: tuple) -> None:
    input_field = driver.find_element(*lacator)
    input_field.send_keys(url)


def get_input_field_text(driver: WebDriver, lacator: tuple) -> str:
    return driver.find_element(*lacator).text


def get_button_text(driver: WebDriver, lacator: tuple) -> str:
    return driver.find_element(*lacator).text


def click_button(driver: WebDriver, lacator: tuple) -> None:
    driver.find_element(*lacator).click()


def wait_for_waiting_process(driver: WebDriver, locator: tuple) -> None:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((locator)))


def wait_for_results(driver: WebDriver, locator: tuple) -> None:
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((locator)))