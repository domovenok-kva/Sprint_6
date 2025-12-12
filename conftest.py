import pytest
from selenium import webdriver
from testdata.testdata import MyURLS


@pytest.fixture
def driver():
    
    driver = webdriver.Firefox()
    driver.get(MyURLS.test_service_url)
    driver.maximize_window()
    yield driver
    driver.quit()