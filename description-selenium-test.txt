api-test  ------api-tests
            |           
            |
            ----selenium-tests
            |           |---> pages
            |                   |
            |                   |----> base_page.py
            |                   |----> contact_us.py
            |                   |----> jobs.py
            |           |---> utils
            |                   |
            |                   |----> locators.py
            |           |
            |           |---> conftest.py
            |           |---> selenium-orfium.py
            |    
            ----conftest.py
            |
            ----geckodriver.exe
            |
            ----chromedriver.exe
            
All tests are contained inside selenium-orfium.py, pages are are contained inside directory pages, and are constructed in distinct .py files, 
there is a base_page.py which contain methods that could be used by different (in this case both) pages.

Locators are described in /selenium-tests/utils/locators.py

api-test/conftest.py::
  sets url for the api-tests 
/selenium-tests/conftest.py ::
    -   contain set up which is to load driver for base page and maximize the window. 
    -   Also accepts the cookie prompt.
    -   configures the browser according to driver (chrome/firefox)
    -   changes the value of url (either from cli either the default to orfium homepage)

both drivers exist in / dir.

selenium-orfium.py ::
---------------------

Contain 3 classes per test

All tests create an object driver which is described by the different pages they are calling,

FIRST TEST :: test_submit_no_info
uses methods from ContactUsPage class
        open_contact_page   ----> opens the page 
        submit_button   --->  clicks on the button  \\\ should assert when locator CHECK_LABEL  is not found!!
        complete_all_required_fields_click   ---> enters value to required fields and clicks submit
        closes the driver
        
        ----- the assertions were not finished --- // incomplete
        
SECOND TEST :: TestJobsPage
uses methods from JobsPage class
            open_jobs_page  ---> opens the page
            follow_career   ---->   follows link to current career
            click_one_job   ---->  clicks on a job with locator JOB1 opens a second window and checks if the window title has changed. Asserts otherwise
            closes the driver
            
THIRD TEST :: test_find_job
uses methods from JobsPage class
            open_jobs_page  ---> opens the page
            follow_career   ---->   follows link to current career
            search_for_job_positive   ---> searches for a keyword that exists, checks if there are results accordingly
            search_for_job_negative    ---->  searches for given keywork "Ninja QA engineer", checks that there are no results as should.
            closes the driver
           
 FAILURE TESTS are failing as instructed..
            

 **In order to get screenshots when failures take place "pytest-failed-screenshot==1.0.2" was installed
 
 
 RUN ::  in root folder (api-test)
         pytest -sv selenium-tests/selenium-orfium.py 
         pytest -sv selenium-tests/selenium-orfium.py -k TestContactUsForm (TestJobsPage / TestSearchJob each test if want to run separately)  
 
 