""" Test Demo Bear website"""
from qaa.init_driver import Initialization
from qaa import bot, constants


class TestDebugBear(Initialization):

    def test_page_load_time(self):
        bot.page_load_time(self.driver)

    def test_check_page_title(self):
        bot.check_title(self.driver)

    def test_check_for_inputed_url(self):
        bot.check_for_inputed_url(self.driver, constants.TEST_URL)

    def test_check_for_start_new_test_button(self):
        bot.check_for_start_test_button(self.driver)

    def test_check_for_start_test_button_text(self):
        bot.check_for_start_button_text(self.driver)

    def test_check_for_waiting_process(self):
        bot.check_for_waiting_process(self.driver, constants.TEST_URL)

    def test_check_for_results(self):
        bot.check_for_results_page(self.driver, constants.TEST_URL)

    def test_check_for_results_elements(self):
        bot.check_for_results_elements(self.driver, constants.TEST_URL)
    
    def test_invalid_url(self):
        bot.invalid_url(self.driver)

    def test_blank_url_field(self):
        bot.blank_url_field(self.driver)



