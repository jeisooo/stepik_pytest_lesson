link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_exist(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")