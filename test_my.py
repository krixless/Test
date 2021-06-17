from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://mail.ru/')
    input_field = driver.find_element_by_xpath("//input[@id='q']")
    input_field.send_keys('python')
    input_field.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.close()