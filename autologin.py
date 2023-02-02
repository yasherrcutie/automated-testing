from selenium import webdriver
from getpass import getpass

username = input("Enter your username: ")
password = getpass("password: ")

driver = webdriver.Chrome("C:\\Dev\\WebDrivers\\chromedriver.exe")
driver.get("http://eclass.wmsu.edu.ph/login/index/")

username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("login-btn")
login_button.submit()
