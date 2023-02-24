from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from LoginPage import LoginPage
import time
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
login_page = LoginPage(driver)
time.sleep(10)
login_page.set_email("bigya.stha")
login_page.set_password("ghdsgsagj")
login_page.click_login()

error = driver.find_element(By.CSS_SELECTOR, 'div._9ay7')
error_message = error.text

try:
    assert error_message == "The password you’ve entered is incorrect."
except AssertionError:
    print("Invalid error message!")

time.sleep(10)
