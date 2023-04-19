import time
from utils.locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class JobsPage(BasePage):
    def __init__(self, driver, url):
        self.locator = Locators
        #contact_url = url + "/contact-us/"
        super().__init__(driver, url)


    def open_jobs_page(self):
        self.open('jobs/')
        time.sleep(1)

    def accept_cookies(self):
        self.wait_element(*self.locator.COOKIE_FORM)
        self.find_element(*self.locator.COOKIE_ACCEPT).click()


    def follow_career(self):
        self.find_element(*self.locator.CURRENT_JOBS).click()


    def click_one_job(self, driver):
        window1 = driver.window_handles[0]
        window1_title = driver.title
        self.find_element(*self.locator.JOB1).click()
        window2 = driver.window_handles[1]
        driver.switch_to.window(window2)
        time.sleep(0.9)
        assert (window1_title!=driver.title), "The page title has not change, when should"

    def search_for_job_positive(self, search_str):
        self.wait_element(*self.locator.SEARCH_JOB)
        self.find_element(*self.locator.SEARCH_JOB).clear()
        time.sleep(0.5)
        self.find_element(*self.locator.SEARCH_JOB).send_keys(search_str)
        self.wait_element(*self.locator.SEARCH_TEST)
        element = self.find_elements(*self.locator.SEARCH_TEST)
        print("Positive test result: ")
        print(element)
        assert (element != []), "The page title has not change, when should"

    def search_for_job_negative(self, search_str):
        self.wait_element(*self.locator.SEARCH_JOB)
        self.find_element(*self.locator.SEARCH_JOB).clear()
        time.sleep(0.5)
        self.find_element(*self.locator.SEARCH_JOB).send_keys(search_str)
        self.wait_element(*self.locator.SEARCH_NINJA)
        element = self.find_elements(*self.locator.SEARCH_NINJA)
        print("Negative test result: ")
        print(element)
        assert (element != []), "This test is meant to fail, no ninja qa"
