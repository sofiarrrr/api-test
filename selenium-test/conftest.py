import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from utils.locators import Locators
from pages.base_page import BasePage

@pytest.fixture(scope='class', autouse=True)
def set_up_tear_down(browser, url):
    locator = Locators
    browser.maximize_window()
    time.sleep(2)
    browser.get(url)
    browser.implicitly_wait(1)
    page = BasePage(driver=browser, url=url)
    page.wait_element(*locator.COOKIE_FORM)
    page.find_element(*locator.COOKIE_ACCEPT).click()
    #page.wait_and_click_element(*locator.COOKIE_ACCEPT)   << if cookie form may not be there
    time.sleep(1)

    # Here's where the tests runs.
    yield

@pytest.fixture(scope='session')
def url(request):
    return "https://orfium.com/"


@pytest.fixture(scope='class')
def browser(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.set_capability('unhandledPromptBehavior', 'accept')
        options.set_capability('unexpectedAlertBehaviour', 'accept')
        if os.name == 'nt':
            browser = webdriver.Chrome(
                executable_path='..\\chromedriver.exe',
                options=options)
        if os.name == 'posix':
            browser = webdriver.Chrome(
                executable_path='chromedriver',
                options=options)
        return browser
    elif browser == 'firefox':
        profile_path = r'C:\Users\rousou\AppData\Roaming\Mozilla\Firefox\Profiles\5reda630.default'
        options=Options()
        options.binary_location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
        options.set_preference('profile', profile_path)
        service = Service(r'..\geckodriver.exe')
        browser = Firefox(service=service, options=options)
        return browser
