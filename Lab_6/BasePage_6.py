import pytest
from _pytest.config import Config
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver

    def visit(self, url, base_url=pytest.config.getoption('base_url')):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(base_url + url)

    def click(self, locator):
        self.find(locator).click()

    def type(self, text, locator):
        self.find(locator).send_keys(text)

    def is_displayed(self, locator, timeout=0):
        try:
            return self.find(locator, timeout).is_displayed()
        except:
            return False

    def find(self, locator):
        return self.find_element(locator)

    def find_element(self, locator):
        by = locator[0]
        value = locator[1]
        return self.driver.find_element(by, value)

    def find(self, locator, timeout=0):
        if timeout == 0:
            return self.find_element(locator)
        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
