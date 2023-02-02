import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_eclass(self, username: str, password: str):
        self.add_input(by=By.ID, value='text', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.CLASS_NAME, value='login-btn')


if __name__ == '__main__':
    browser = Browser('drivers/chromedriver')

    browser.open_page('http://eclass.wmsu.edu.ph/')
    time.sleep(3)

    browser.login_eclass(username='xt202003931@wmsu.edu.ph', password='Amingyasher2020*')
    time.sleep(10)

    browser.close_browser()
