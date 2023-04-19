
api-test  ------api-tests
            |           |----> conftest.py
            |           |----> get_check_api.py
            |           |----> test_api_status.py
            |
            ----selenium-tests
            |
            |
            ----conftest.py
            |
            |
            ----geckodriver.exe
            |
            ----chromedriver.exe
            


api-tests
=================

get_check_api.py :: a class wich initiates itself with url and has two methods get_response_ok_api and get_data_json both use the requests package to get api data using GET request 
test_api_status.py :: contain the tests, 3 static tests under class TestOrfium, 

All three tests create an object getCheckApi, calling get_check_api.py


First Test:: test_call_status 
uses method get_response_ok_api to get the response status of the url, 
asserts in case the response status is NOK !=200

Second Test:: test_get_title
uses method get_data_json to get the json data out of the api, then prints the title when it exists, 
asserts Title is empty when title does not exist, and asserts No key when title key does not exist at all.

Third Test:: test_get_artist
uses method get_data_json to get the json data out of the api, then prints the artists names when they exist, 
asserts per initial id when artists key is empty, and assetys Has no key when artists key does not exist at all.

api-test/conftest.py::
  sets url for the api-tests 
api-test/api-tests/conftest.py
    return the default value without changing it


 To RUN test and get allure result::
    py.test --alluredir=%allure_result_folder% ./api-tests
    pytest -sv --alluredir=%allure_result_folder% ./api-tests
    
    
 FAILURE TESTS are failing as instructed..