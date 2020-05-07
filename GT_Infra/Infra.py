"""
This file was created for fun
Author:
    v-daeder - Dana Eder
Date:

Purpose:
    
"""

from selenium import webdriver
from time import sleep
import pytest
import logging

logging.basicConfig(filename="tests_logs.log", filemode='w', format='%(asctime)s  - %(message)s', level=logging.INFO)
logger = logging.getLogger('log')


def open_google():
    url = 'https://translate.google.com/'
    global browse
    browse = webdriver.Chrome()
    try:
        browse.get(url)
    except Exception as e:
        logger.error(f"Error While opening browser {e}")
    sleep(5)
    return browse


def press_keys(browse, keys_to_press):
    """

    :param keys_to_press: dict of words and their value
    browse(webdriver.Chrome):
    :return:
    """
    flag = True
    element = browse.find_element_by_id("source")
    for word in keys_to_press.keys():
        element.send_keys(word)
        sleep(5)
        result = browse.find_element_by_class_name("result-shield-container").text
        if keys_to_press[word] != result:
            print(f"{result} is not {keys_to_press[word]}")
            logger.error(f"{result} is not {keys_to_press[word]}")
            flag = False
        clear_data(browse)
    return flag


def close_web(browse):
    """

    :param browse(webdriver.Chrome):
    :return:
    """
    browse.close()


def clear_data(browse):
    """

    :param browse(webdriver.Chrome):
    :return:
    """
    clear = browse.find_element_by_class_name("clear-wrap")
    clear.click()


def info_log(data_to_log):
    """

    :param data_to_log:
    :return:
    """
    logger.info(f"{data_to_log}")


def check_history(browse):
    element = browse.find_element_by_id("ft-icon-img-hst")
    assert element.click()==None, "History is unavailable "


def clear_history(browse):
    """

    :param browse(webdriver.Chrome):
    :return:
    """
    # clear = browse.find_element_by_class_name(
    #     "history-features")
    # clear.click()
    # # img = browse.find_element_by_class_name("placeholder-image")
    # # assert img, "Error in clear history"
