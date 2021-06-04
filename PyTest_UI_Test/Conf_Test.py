# Import the 'modules' that are required for execution for Selenium test automation

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init","app_url")
class BasicTest:
    pass

@pytest.fixture():
def app_url():
	url="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
	return url