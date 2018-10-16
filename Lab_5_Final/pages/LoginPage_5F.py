from selenium.webdriver.common.by import By

from Lab_5_Final.pages.BasePage_5F import Page


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

    def enter_username(self, username):
        self.type(username, self.username_field)

    def enter_password(self, password):
        self.type(password, self.password_field)

    def submit(self):
        self.click(self.submit_button)

    def success_message_present(self):
        return self.is_displayed(self.success_message, 3)

    def error_message_present(self):
        return self.is_displayed(self.error_message, 3)