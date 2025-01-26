from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

alert = browser.switch_to.alert
alert.accept()

x = int(browser.find_element(By.ID, "input_value").text)
x = log(abs(12 * sin(x)))

answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(x))

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(5)
browser.quit()
