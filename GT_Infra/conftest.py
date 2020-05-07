"""
This file was created for fun
Author:
    Dana Eder
Date:

"""
from Infra import *


@pytest.fixture
def test_handler(request):
    info_log(f"Test - {request.function.__name__} Starts")
    browse = open_google()
    yield browse

    def close_session():
        info_log(f"Test - {request.function.__name__} Finished Successfully")
        close_web(browse)

    request.addfinalizer(close_session)
