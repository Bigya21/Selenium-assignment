from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
# open web browser
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
# open url
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME, "email").send_keys("bigya.stha")
driver.find_element(By.NAME, "pass").send_keys("ghdsgsagj")
driver.find_element(By.NAME, "login").click()
time.sleep(10)
