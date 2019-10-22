import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import config

options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(options=options, firefox_profile=profile)
url = config.PLC_URL

try:
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Login_Area_Form')))
except TimeoutException:
    print('Timeout waiting for page loading')

element = driver.find_element_by_name('Login')
element.send_keys(config.PLC_USERNAME)


element = driver.find_element_by_name('Password')
element.send_keys(config.PLC_PASSWORD)

element = driver.find_element_by_id('login_box_button')
element.click()

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Stop')))
except TimeoutException:
    print('Timeout waiting for page loading')

element = driver.find_element_by_id('Stop')
element.click()

time.sleep(1)

element = driver.find_element_by_id('Run')
element.click()

driver.quit()
