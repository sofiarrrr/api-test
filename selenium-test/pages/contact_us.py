import time
from utils.locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ContactUsPage(BasePage):
    def __init__(self, driver, url):
        self.locator = Locators
        #contact_url = url + "/contact-us/"
        super().__init__(driver, url)


    def open_contact_page(self):
        self.open('contact-us/')
        time.sleep(1)

    def accept_cookies(self):
        self.wait_element(*self.locator.COOKIE_FORM)
        self.find_element(*self.locator.COOKIE_ACCEPT).click()

    def submit_button(self, driver):
        self.scroll_to_element_and_click(driver, *self.locator.INQUIRY_SUBMIT_BUT)

    def wait_for_check_label(self):
        self.wait_element(self.locator.CHECK_LABEL)

    def complete_all_required_fields_click(self, driver, first_name, last_name, email, company_name, message):
        self.find_element(*self.locator.INQUIRY_FORM)
        self.find_element(*self.locator.FIRST_NAME).send_keys(first_name)
        self.find_element(*self.locator.LAST_NAME).send_keys(last_name)
        self.find_element(*self.locator.EMAIL).send_keys(email)
        self.find_element(*self.locator.COMPANY_NAME).send_keys(company_name)
        select_business_type = Select(self.find_element(*self.locator.BUSINESS_TYPE_DRDN))
        select_business_type.select_by_visible_text('Broadcaster')
        time.sleep(1)
        select_inquiry_reason = Select(self.find_element(*self.locator.INQUIRY_REASON))
        select_inquiry_reason.select_by_visible_text('I want to work for Orfium')
        time.sleep(1)
        self.find_element(*self.locator.MESSAGE_INPUT).send_keys(message)
        self.scroll_to_element_and_click(driver, *self.locator.LEGAL_CONSENT_CHK)
        time.sleep(5)
        #self.wait_and_click_element(*self.locator.LEGAL_CONSENT_CHK)
