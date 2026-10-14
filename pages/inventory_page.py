from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def wait_until_loaded(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.TITLE)
        ).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text
