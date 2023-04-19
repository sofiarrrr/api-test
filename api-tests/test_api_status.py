import requests
import json
import sys
from get_check_api import getCheckApi
import pytest
from pytest_check import check

class TestOrfium:

    @staticmethod
    def test_call_status(url):
        resp = getCheckApi(url=url)
        response = resp.get_response_ok_api()
        assert (response == 200), "Response is not ok:200, it has status code: " + response

    @staticmethod
    def test_get_title(url):
        resp = getCheckApi(url=url)
        key = 'title'
        get_song_data = resp.get_data_json()
        for song_id in get_song_data:
            try:
                if (get_song_data[song_id][key]):
                    print(get_song_data[song_id][key])
                else:
                    with check.raises(AssertionError):
                        print("Title is empty")
            except:
                print('No key')

    @staticmethod
    def test_get_artist(url):
        resp = getCheckApi(url=url)
        key = 'artists'
        get_song_data = resp.get_data_json()
        for song_id in get_song_data:
            try:
                if (get_song_data[song_id][key] != []):
                    print(get_song_data[song_id][key])
                else:
                    with check.raises(AssertionError):
                        print(song_id + " Artists are empty")
            except KeyError:
                with check.raises(AssertionError):
                    print(song_id + ' Has No key')
