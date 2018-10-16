from Lab_4.LoginPage_4 import LoginPage


def test_login(selenium):
    login = LoginPage()

    # TODO: Follow Lab 4 to refactor to use Page Objects
    selenium.get("http://the-internet.herokuapp.com/login")
    selenium.find_element_by_id("username").send_keys("tomsmith")
    selenium.find_element_by_id("password").send_keys("SuperSecretPassword!")
    selenium.find_element_by_css_selector("#login button[type='submit']").click()
    assert selenium.find_element_by_css_selector(".flash.success").is_displayed()