from selenium.webdriver.common.by import By
from login_page import LoginPage
from base_page import Basepage
from base_data import Base_URL, Valid_Password, Valid_Username, Invalid_Username, Invalid_Password

class LoginPage(Basepage):
    def test_login_valid_data(self):
        self.driver = (Base_URL)
        login_page = LoginPage(self.driver)
        login_page = (Valid_Username, Valid_Password)
        # Add assertions for successful signup
        assert login_page() == "Login Successfull"

    def test_login_invalid_data(self):
        self.driver = (Base_URL)
        login_page = LoginPage(self.driver)
        login_page = (Invalid_Username, Invalid_Password)
        # Add assertions for error message
        assert login_page() == "Login Failed"