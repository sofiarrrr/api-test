import requests
import json
import sys

class getCheckApi:
    def __init__(self, url):
        self.url = url

    def get_response_ok_api(self):
        response = requests.get(self.url)
        return response.status_code

    def get_data_json(self):
        get_response = requests.get(self.url)
        get_data = get_response.json()
        return get_data
