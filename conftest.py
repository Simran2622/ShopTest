import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Start a fresh Chrome browser for each test."""
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)  # Selenium Manager handles the driver
    browser.get("https://www.saucedemo.com/")
    yield browser
    browser.quit()
