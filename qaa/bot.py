from selenium.webdriver.remote.webdriver import WebDriver

from qaa import constants
from qaa.page_object import page, locator


def page_load_time(driver: WebDriver) -> None:
    page.open_page(driver, constants.VALID_URL)
    assert driver.execute_script("return performance.timing.loadEventEnd - performance.timing.navigationStart") < 1500


def check_title(driver: WebDriver) -> None:
    page.open_page(driver, constants.VALID_URL)
    assert driver.title == 'Free Website Speed Test | DebugBear', 'Title does not match.'


def fill_in_url_field(driver: WebDriver, url: str) -> None:
    page.open_page(driver, constants.VALID_URL)
    page.input_field(driver, url, locator.INPUT_FIELD)
    assert page.get_input_field_text(driver, locator.INPUT_FIELD) != '', 'Field is empty.'


def check_for_inputed_url(driver: WebDriver, url: str) -> None:
    page.open_page(driver, constants.VALID_URL)
    page.input_field(driver, url, locator.INPUT_FIELD)
    assert page.get_input_field_text(driver, locator.INPUT_FIELD) == constants.TEST_URL, 'URL does not match.'


def check_for_start_test_button(driver: WebDriver) -> None:
    page.open_page(driver, constants.VALID_URL)
    button = page.get_element(driver, locator.BUTTON_START_TEST)
    assert button is not None, 'Button does not match.'


def check_for_start_button_text(driver: WebDriver) -> None:
    page.open_page(driver, constants.VALID_URL)
    button_text = page.get_button_text(driver, locator.BUTTON_START_TEST)
    assert button_text == 'Start Test', 'Button does not match.'

def check_for_waiting_process(driver: WebDriver, url: str) -> None:
    page.open_page(driver, constants.VALID_URL)
    page.wait_for_page_to_load(driver, locator.MAIN_TITLE)
    page.input_field(driver, url, locator.INPUT_FIELD)
    page.click_button(driver, locator.BUTTON_START_TEST)
    page.wait_for_waiting_process(driver, locator.WAITING_BAR)
    waiting_process = page.get_waiting_process_text(driver, url)
    assert waiting_process == 'Testing https://es.idoven.ai/', 'Waiting process does not match.'


def check_for_results_page(driver: WebDriver, url: str) -> None:
    page.open_page(driver, constants.VALID_URL)
    page.wait_for_page_to_load(driver, locator.MAIN_TITLE)
    page.input_field(driver, url, locator.INPUT_FIELD)
    page.click_button(driver, locator.BUTTON_START_TEST)
    page.wait_for_results(driver, locator.METRIC_OVERVIEW)
    netloc = page.get_netloc_from_url(url)
    assert driver.title == netloc + ' | DebugBear', 'Title does not match.' 


def check_for_results_elements(driver: WebDriver, url: str) -> None:
    page.open_page(driver, constants.VALID_URL)
    page.wait_for_page_to_load(driver, locator.MAIN_TITLE)
    page.input_field(driver, url, locator.INPUT_FIELD)
    page.click_button(driver, locator.BUTTON_START_TEST)
    page.wait_for_results(driver, locator.METRIC_OVERVIEW)
    for element in locator.RESULT_ELEMENTS:
        assert page.get_element(driver, element) is not None, 'Element does not match.'


def invalid_url(driver: WebDriver) -> None:
    page.open_page(driver, constants.INVALID_URL)
    assert driver.title == 'Free Website Speed Test | DebugBear', 'Title does not match.'


def blank_url_field(driver: WebDriver) -> None:
    page.open_page(driver, constants.VALID_URL)
    page.wait_for_page_to_load(driver, locator.MAIN_TITLE)
    page.click_button(driver, locator.BUTTON_START_TEST)
    alert_message = page.get_element(driver, locator.EMPTY_FIELD)
    assert alert_message is not False, 'Alert message does not match.'


