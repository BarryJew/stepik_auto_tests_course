from selenium import webdriver
from selenium.webdriver.common.by import By
import time

links = [
    "http://suninjuly.github.io/registration1.html",
    "http://suninjuly.github.io/registration2.html",
]

for link in links:
    try:

        browser = webdriver.Chrome()
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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        print("pass!")

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

        # не забываем оставить пустую строку в конце файла
