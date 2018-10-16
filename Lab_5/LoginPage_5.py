from selenium.webdriver.common.by import By

from pages.BasePage import Page


class LoginPage(Page):

    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    submit_button = (By.CSS_SELECTOR, "#login button[type='submit']")

    success_message = (By.CSS_SELECTOR, "#flash.success")
    error_message = (By.CSS_SELECTOR, "#flash.error")

    def __init__(self, driver):
        super().__init__(driver)
        self.visit("/login")



    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.submit()

    def success_message_present(self):
        return self.driver.find_element(self.success_message).is_displayed()

    def error_message_present(self):
        return self.driver.find_element(self.error_message).is_displayed()