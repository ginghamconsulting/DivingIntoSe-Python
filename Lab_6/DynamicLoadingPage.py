from Lab_6.BasePage import Page


class DynamicLoadingPage(Page):

    start_button = (By.CSS_SELECTOR, "#start button")
    finish_text = (By.ID, "finish")

    def __init__(self, driver, example_number):
        super().__init__(driver)
        self.visit("/dynamic_loading/" + str(example_number))
        self.click(self.start_button)

    def finish_text_present(self):
        return self.is_displayed(self.finish_text, 10)