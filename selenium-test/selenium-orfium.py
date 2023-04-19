import time
import re
import pytest
from pages.contact_us import ContactUsPage
from pages.jobs import JobsPage


class TestContactUsForm:

    @staticmethod
    def test_submit_no_info(browser, url):
        page = ContactUsPage(driver=browser, url=url)
        page.open_contact_page()
        page.submit_button(browser)
        print("submit buttOn")
        page.complete_all_required_fields_click(browser, "name", "last_name", "myname@gmail.com", "company_name", "message")
        print("submit buttOn")
        browser.close()


class TestJobsPage:

    @staticmethod
    def test_check_career_page(browser, url):
        page = JobsPage(driver=browser, url=url)
        page.open_jobs_page()
        page.follow_career()
        time.sleep(2)
        page.click_one_job(browser)
        browser.close()


class TestSearchJob:

    @staticmethod
    def test_find_job(browser, url):
        page = JobsPage(driver=browser, url=url)
        page.open_jobs_page()
        page.follow_career()
        time.sleep(1)
        page.search_for_job_positive('test')   #('Ninja QA engineer')
        time.sleep(1)
        page.search_for_job_negative('Ninja QA engineer')
