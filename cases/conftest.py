import pytest
from selenium import webdriver
from config.config import *

@pytest.fixture(scope="session")
def login():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()