import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    message = ""
    lessons = ["236895","236896","236897","236898","236899","236903","236904","236905"]
    @pytest.mark.parametrize('lesson', lessons)
    def test_links(self,browser,lesson):
        input_text = str(math.log(int(time.time())))
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        login = "login"
        password = "password"
        browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form__btn"))).click()
        time.sleep(10)
        
        textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")
        textarea.send_keys(input_text)
        submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        submit.click()
        time.sleep(5)
        answer = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text
        print(answer)
        assert "Correct!" in answer
        if answer != "Correct!":
            self.message += answer
    print(message)

if __name__ == "__main__":

    pytest.main()
# Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе запустились с заданными параметрами. 
# В таком случае отметка о параметризации должна быть перед объявлением класса: 

#@pytest.mark.parametrize('language', ["ru", "en-gb"])
#class TestLogin:
#    def test_guest_should_see_login_link(self, browser, language):
#        link = f"http://selenium1py.pythonanywhere.com/{language}/"
#        browser.get(link)
#        browser.find_element(By.CSS_SELECTOR, "#login_link")
#        # этот тест запустится 2 раза
#
#    def test_guest_should_see_navbar_element(self, browser, language):
#        # этот тест тоже запустится дважды