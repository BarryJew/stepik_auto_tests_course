from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, "input_value")
x = int(x.text)
x = log(abs(12 * sin(x)))

answer = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(str(x))

checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()

radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)
browser.quit()
