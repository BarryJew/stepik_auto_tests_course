from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_has_add_button(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert btn is not None, "Кнопка добавления товара отсутствует"


# pytest -s -v --browser_name=chrome test_parser.py
