"""
This file was created for tw
Author:
    Dana Eder
Date:
 28/01/2020
Purpose:
    Prove Automation Skills
"""
import json

import requests

IP = "35.192.16.242"
LOCAL_URL = 'http://localhost:8000/players?page='
USER = 'admin'
TOKEN = 'admin'


class TwtaskAPI(object):
    def __init__(self):
        self.gist_sha = None
        self.gist_id = None

    def post(self,final_path):
        data = {"Name": "Dana", "ID": 33}
        return requests.post(final_path, auth=(USER, TOKEN), json=data)

    def get(self, final_path):
        return requests.get(url=final_path, auth=(USER, TOKEN))


t = TwtaskAPI()
if '__main__' == __name__:
    final_path=LOCAL_URL+'2'
    response = t.get(final_path)
    print(t.get(final_path))
    print(t.post(final_path))
    print(json.loads(t.get(final_path).content.decode('utf-8')))


def test_post():
    """
    This API shouldn't allow 'post'
    Returns:
        return must be other then 200
    """
    final_path=LOCAL_URL+'2'
    print(t.post(final_path))

def test_invalid_page():
    """
    no page number
    Returns:
        print the final result

    """
    print(t.get(LOCAL_URL))