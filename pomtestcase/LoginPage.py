from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = ("name", "email")
        self.password_field = ("name", "pass")
        self.login_button = ("name", "login")


    def set_email(self, email):
        email_field = self.driver.find_element(self.email_field[0], self.email_field[1])
        email_field.send_keys(email)

    def set_password(self, password):
        password_field = self.driver.find_element(self.password_field[0], self.password_field[1])
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(self.login_button[0], self.login_button[1])
        login_button.click()

