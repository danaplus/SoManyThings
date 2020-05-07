"""
This file was created for fun
Author:
     Dana Eder
Date:

Purpose:
    
"""
import json

JSON_FILE = r'C:\Users\v-daeder\Downloads\record_record_2019-09-24_17_44_58\record_record_2019-09-24_17_44_58.json'


def open_json():
    counter = 0
    with open(JSON_FILE) as a:
        my_data = json.loads(a.read())
    for data in my_data:
        if 'querySource' in data:
            if data['querySource'] == 'Live':
                counter += 1
            print(data['querySource'])
    print(counter)


if __name__ == '__main__':
    open_json()
