from selenium.webdriver.common.by import By
from base_page import Basepage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(Basepage):
    username_field = (By.ID, 'loginusername')
    password_field = (By.ID, 'loginpassword')
    login_button = (By.XPATH, "//button[@onclick = 'logIn()']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # def wait_for_element(self, locator):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.username_field))
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.password_field))
        WebDriverWait(self.login_button,8).until(EC.element_to_be_clickable(self.login_button))
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()