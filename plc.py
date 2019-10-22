import sys

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PlcHandler:
    def __init__(self):
        options = Options()
        options.headless = True
        profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox(options=options,
                                        firefox_profile=profile)

    def login(self, *, url, username, password, ttl=10):
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, ttl).until(
                EC.presence_of_element_located((By.ID, 'Login_Area_Form')))
        except TimeoutException:
            print('Timeout waiting for page loading')
            sys.exit()
        element = self.driver.find_element_by_name('Login')
        element.send_keys(username)
        element = self.driver.find_element_by_name('Password')
        element.send_keys(password)
        element = self.driver.find_element_by_id('login_box_button')
        element.click()
        try:
            WebDriverWait(self.driver, ttl).until(
                EC.presence_of_element_located((By.ID, 'Stop')))
        except TimeoutException:
            print('Timeout waiting for page loading')
            sys.exit()

    def run(self):
        element = self.driver.find_element_by_id('Run')
        element.click()

    def stop(self):
        element = self.driver.find_element_by_id('Stop')
        element.click()

    def __del__(self):
        self.driver.quit()
