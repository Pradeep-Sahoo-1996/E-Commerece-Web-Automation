import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        request.cls.driver = driver
        return driver
    except Exception as e:
        print(f"Error initializing ChromeDriver: {e}")
        return None


#Report Generate
# pytest --html=reports/Pytest.html --self-contained-html
