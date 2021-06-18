from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import allure


@allure.title('test_google_search')
def test_google_search():
    with allure.step('Starting'):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://mail.ru/')
        input_field = driver.find_element_by_xpath("//input[@id='q']")
        input_field.send_keys('python')
        input_field.send_keys(Keys.ENTER)
    with allure.step('Closing'):
        driver.close()
