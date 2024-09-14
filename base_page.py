from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:
    def __init__ (self, driver):
        self.driver = driver

    def wait_for_element(self,by, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by, locator))

    def click_element(self, by, locator):
        self.wait_for_element(by, locator)
        element = self.driver.find_element(by, locator)
        element.click()


