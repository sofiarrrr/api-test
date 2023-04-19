from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Locators:

    COOKIE_FORM = (By.XPATH, '//*[@id="cookie-law-info-bar"]')
    COOKIE_ACCEPT = (By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')

    INQUIRY_FORM = (By.XPATH, '//*[@id="hsForm_254e2055-1227-4703-a29b-4100eb37d66c"]')
    INQUIRY_SUBMIT_BUT = (By.XPATH, "//input[@type='submit']")
    SUBMIT_FORM = (By.XPATH, '//div[contains(@class, "actions")]')
    #INQUIRY_SUBMIT_BUT = (By.XPATH, '/html/body/main/div/div[1]/div/div[1]/div[2]/form/div[3]/div[2]/input')

    FIRST_NAME = (By.XPATH, '//*[@id="firstname-254e2055-1227-4703-a29b-4100eb37d66c"]')
    LAST_NAME = (By.XPATH, '//*[@id="lastname-254e2055-1227-4703-a29b-4100eb37d66c"]')
    EMAIL = (By.XPATH, '//*[@id="email-254e2055-1227-4703-a29b-4100eb37d66c"]')
    COMPANY_NAME = (By.XPATH, '//*[@id="company-254e2055-1227-4703-a29b-4100eb37d66c"]')
    BUSINESS_TYPE_DRDN = (By.XPATH, '//*[@id="business_type-254e2055-1227-4703-a29b-4100eb37d66c"]')
    INQUIRY_REASON = (By.XPATH, '//*[@id="0-2/inquiry_reason-254e2055-1227-4703-a29b-4100eb37d66c"]')

    MESSAGE_INPUT = (By.XPATH, '//*[@id="message-254e2055-1227-4703-a29b-4100eb37d66c"]')

    LEGAL_CONSENT_CHK = (By.XPATH, '//*[@id="LEGAL_CONSENT.subscription_type_12401388-254e2055-1227-4703-a29b-4100eb37d66c"]')

    CHECK_LABEL = (By.XPATH, "//label[contains(text(), 'Please complete all required fields.')]")


#############################

    CURRENT_JOBS = (By.XPATH, "//*[contains(text(), 'Explore all jobs')]")
    #DEV_JOB = (By.XPATH, "//*[contains(text(), 'Explore all jobs')]")
    JOB1 = (By.XPATH, "//div[@data-key='3']")


    SEARCH_JOB = (By.XPATH, "//input[@name='search']")
    SEARCH_NINJA = (By.XPATH, "//div[contains(@class, 'job-position') and contains(text(), 'Ninja QA engineer')]")
    SEARCH_TEST = (By.XPATH, "//div[contains(@class, 'job-position') and contains(text(), 'Test')]")

    "//div[contains(@class, 'job-position') and contains(text(), 'Ninja QA engineer')]"
