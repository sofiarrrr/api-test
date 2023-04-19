"""Base Page Class inherited from every other page object."""
import time
import uuid

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    Base Page object.

    Page objects are based on and inherit basic methdods and
    attributes of this class.
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.timeout = 30
        self.url = url

    def __set__(self, field, value):
        """Set the text to the value supplied."""
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(*self.locator.field))
        self.driver.find_element_by_name(*self.locator.field).clear()
        self.driver.find_element_by_name(*self.locator.field).send_keys(value)

    def __get__(self, field):
        """Get the text of the specified object."""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(*self.locator.field))
        element = driver.find_element_by_name(*self.locator.field)
        return element.get_attribute("value")

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def check_element(self, *locator):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            pass

    def wait_and_click_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator))
            self.find_element(*locator).click()
        except TimeoutException:
            pass

    def open(self, path):
        target_url = self.url + path
        self.driver.get(target_url)
        self.driver.maximize_window()
        time.sleep(5)

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def scroll_to_element_and_click(self, driver, *locator):
        element = self.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

        def close(self, driver):
            """Clicks close button."""
            driver.close()
            time.sleep(0.5)
