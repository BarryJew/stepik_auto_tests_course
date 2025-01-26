from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

elements = browser.find_elements(By.TAG_NAME, "input")
name = elements[0]
name.send_keys("Ivan")
last = elements[1]
last.send_keys("Sap")
email = elements[2]
email.send_keys("loltest@test.ru")

fileInsert = elements[3]
dirPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(dirPath, "test.txt")
fileInsert.send_keys(filePath)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)
browser.quit()
