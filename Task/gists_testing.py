"""
This file was created for Intsights
Author:
    Dana Eder
Date:
 23/01/2020
Purpose:
    Prove Automation Skills
"""
import json

import pytest
import requests

GIST_URL = 'https://api.github.com/gists'
USER = 'danaplus'
TOKEN = '76e50d5fc728b402e5530576e7463cce5ed27678'


class GistAPI(object):
    def __init__(self):
        self.gist_sha = None
        self.gist_id = None

    def post(self, file_name, description, content, public=True):
        data = {
            "description": description,
            "public": public,
            "files": {
                file_name: {
                    "content": content
                }
            }
        }
        return requests.post(GIST_URL, auth=(USER, TOKEN), json=data)

    def get(self, arguments):
        new_url = GIST_URL + arguments
        return requests.get(url=new_url)

    def put(self, arguments):
        new_url = GIST_URL + arguments
        return requests.put(url=new_url, headers={'content-length': '0'})

    def delete(self, arguments):
        new_url = GIST_URL + arguments
        return requests.delete(url=new_url)  # , headers={'content-length': '0'})

    def patch(self, file_name, description, content, id):
        data = {
            "description": description,
            "files": {
                file_name: {
                    "content": content,
                    "filename": file_name
                }
            }
        }
        return requests.patch(url=GIST_URL + f'/{id}', auth=(USER, TOKEN), json=data)


gists_api = GistAPI()


def test_list_user_gists():
    result = gists_api.get('/public')
    result_dict = json.loads(result.content.decode('utf-8'))
    assert result.status_code == 200, 'Get msg Failed!'
    for item in result_dict:
        for key, value in item.items():
            print(key, value)


def test_create_new_gist():
    result = gists_api.post('dana.py', "I'm Awsom", "print('I just learned RESTAPI')")

    assert result.status_code == 201, 'Post msg Failed!'
    result_dict = json.loads(result.content.decode('utf-8'))
    gists_api.gist_id = result_dict['id']
    for key, value in result_dict.items():
        print(key, value)


def test_edit_last_git():
    assert gists_api.gist_id, "No gist_id"
    result = gists_api.patch('dana.py', "2I'm Awsom", "print('I just learned RESTAPI')", gists_api.gist_id)
    assert result.status_code == 200, 'Patch msg Failed!'


def test_get_revision():
    assert gists_api.gist_id, "No gist_id"
    result = gists_api.get(f'/{gists_api.gist_id}')
    assert result.status_code == 200, 'Get msg Failed!'


@pytest.mark.xfail
def test_start_git():
    assert gists_api.gist_id, "No gist_id"
    result = gists_api.put(f'/{gists_api.gist_id}/star')
    assert result.status_code == 204, 'Star msg Failed!' % json.loads(result.content.decode('utf-8'))


@pytest.mark.xfail
def test_delete_star():
    assert gists_api.gist_id, "No gist_id"
    result = gists_api.delete(f'/{gists_api.gist_id}/star')
    assert result.status_code == 204, 'Star delete msg Failed!' % json.loads(result.content.decode('utf-8'))
