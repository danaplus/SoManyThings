"""
This file was created for me
Author:
    Dana Eder
Date:
10/03/2020
Purpose:
    fun
"""
import json
import urllib.parse
import operator

import requests

QA_JSON = 'https://anzu-assets.s3.amazonaws.com/qa.json'

if __name__ == '__main__':
    count = 0
    types = {}
    re = requests.get(QA_JSON)
    json_dict = json.loads(re.content.decode('utf-8'))
    if json_dict['files']:
        base_url = json_dict['base_url']
        for file in json_dict['files']:
            event_file = urllib.parse.urljoin(base_url, file)
            req = requests.get(event_file)
            json_list = json.loads(req.content.decode('utf-8'))
            count += len(json_list)
            for dict_obj in json_list:
                ty = dict_obj['type']
                if ty in types:
                    types[ty] += 1
                else:
                    types[ty] = 1

    index, value = max(enumerate(types.values()), key=operator.itemgetter(1))
    hi_ty=types.keys()
    print(f"Number of events: {count}, \n count by type: {types},with the value {value} ")
