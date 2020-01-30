"""
This file was created for Chegg
Author:
    v-daeder - Dana Eder
Date:

Purpose:
    
"""

from Infra import *
import conftest

global browse
words_dict = {r'בננה': 'Banana',
              r'תפוח': 'an Apple',
              r'מלפפון': 'cucumber',
              r'עגבניה': 'tomato'}


def test_translate_sanity(test_handler):
    result = press_keys(test_handler, words_dict)
    assert result, logger.error(f"Test - {test_translate_sanity.__name__} Fails")


def test_detect_lang(test_handler):
    words_dict = {r'בננה': 'Banana',
                  'Apple': 'Apple',
                  r'מלפפון': 'cucumber',
                  'помидор': 'a tomato'}
    result = press_keys(test_handler, words_dict)
    assert result, logger.error(f"Test - {test_detect_lang.__name__} Fails")


def test_clear_history(test_handler):
    result = press_keys(test_handler, words_dict)
    assert result, logger.error(f"Test - {test_clear_history.__name__} Fails")
    check_history(test_handler)
