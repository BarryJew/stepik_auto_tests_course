# Общее правило для всех фреймворков: название тестового метода должно начинаться со слова "test_". 
# Для unittest существуют собственные дополнительные правила:
# - Тесты обязательно должны находиться в специальном тестовом классе.
# - Вместо assert должны использоваться специальные assertion методы.

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def use_link(link, browser):
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first.send_keys("Мой ответ")

    second = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    second.send_keys("Мой ответ")

    third = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    third.send_keys("Мой ответ")

    first_2 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    first_2.send_keys("Мой ответ")

    second_2 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    second_2.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text

    

class TestLinks(unittest.TestCase):
    def test_link1(self):
        browser = webdriver.Chrome()
        result = use_link("http://suninjuly.github.io/registration1.html", browser)
        self.assertEqual(result, "Congratulations! You have successfully registered!", "No such element")
        browser.quit()

    def test_link2(self):
        browser = webdriver.Chrome()
        result = use_link("http://suninjuly.github.io/registration2.html", browser)
        self.assertEqual(result, "Congratulations! You have successfully registered!", "No such element")
        browser.quit()

if __name__ == "__main__":
    unittest.main()


