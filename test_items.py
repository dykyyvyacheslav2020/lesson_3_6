import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_button(browser):
    browser.get(link)
    time.sleep(30)
    add_button = browser.find_element_by_class_name("btn-add-to-basket")
    button = add_button.text
    assert len(button) > 0

