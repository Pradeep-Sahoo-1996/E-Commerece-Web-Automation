from selenium.webdriver.common.by import By
from base_page import Basepage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage(Basepage):
    username_field = (By.ID, 'sign-username')
    password_field = (By.ID, 'sign-password')
    signup_button = (By.XPATH, "//button[@onclick = 'register()']")

    def __init__(self, driver):
        self.driver = driver

    def signup(self, username, password):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.username_field))
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.password_field))
        WebDriverWait(self.signup_button,8).until(EC.element_to_be_clickable(self.signup_button))
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.signup_button)