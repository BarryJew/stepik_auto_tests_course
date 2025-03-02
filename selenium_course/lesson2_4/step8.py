from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
book_btn = browser.find_element(By.ID, "book")
book_btn.click()

x = int(browser.find_element(By.ID, "input_value").text)
x = str(log(abs(12 * sin(x))))

browser.find_element(By.ID, "answer").send_keys(x)

browser.find_element(By.ID, "solve").click()

time.sleep(5)
browser.quit()
