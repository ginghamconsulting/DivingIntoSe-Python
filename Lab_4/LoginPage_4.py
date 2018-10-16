from selenium.webdriver.common.by import By


class LoginPage():

    # TODO: Follow Lab 4 Directions

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """
        Simple method to force the tuple to be recognized as a tuple to then send it properly to Selenium.
        Use self.find_element() instead of self.driver.find_element()
        :param locator: a tuple of the locator strategy and value. Example (By.ID, "SomeId")
        :return: WebElement
        """
        by = locator[0]
        value = locator[1]
        return self.driver.find_element(by, value)
