from Lab_6.DynamicLoadingPage import DynamicLoadingPage


def test_hidden_element_loads(selenium):
    dynamic = DynamicLoadingPage(selenium, "1")
    assert dynamic.finish_text_present()

def test_element_appears(selenium):
    dynamic = DynamicLoadingPage(selenium, "2")
    assert dynamic.finish_text_present()