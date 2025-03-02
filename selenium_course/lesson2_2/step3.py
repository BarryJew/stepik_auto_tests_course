from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")

    # Ваш код, который заполняет обязательные поля
    num1_element = browser.find_element(By.ID, "num1")
    num1 = int(num1_element.text)

    num2_element = browser.find_element(By.ID, "num2")
    num2 = int(num2_element.text)

    answer_num = num1 + num2
    print(answer_num)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(answer_num))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
