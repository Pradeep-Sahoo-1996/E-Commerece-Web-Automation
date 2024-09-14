import pytest
from signup_page import SignupPage
from base_page import Basepage
from base_data import Base_URL, Valid_Password, Valid_Username, Invalid_Username, Invalid_Password

@pytest.mark.usefixtures("setup")
class SignupPage(Basepage):
    def test_signup_with_valid_data(self):
        self.driver = (Base_URL)
        signup_page = SignupPage(self.driver)
        signup_page = (Valid_Username, Valid_Password)
        # Add assertions for successful signup
        assert signup_page() == "Signup successful"

    def test_signup_with_invalid_data(self):
        self.driver = (Base_URL)
        signup_page = SignupPage(self.driver)
        signup_page = (Invalid_Username, Invalid_Password)
        # Add assertions for error message
        assert signup_page() == "Signup Failed"
