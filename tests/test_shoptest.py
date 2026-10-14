from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_valid_login_opens_products_page(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.wait_until_loaded() == "Products"

def test_invalid_password_shows_error(driver):
    login = LoginPage(driver)
    login.login(USERNAME, "wrong_password")

    assert "Username and password do not match" in login.error_message()

def test_empty_username_is_rejected(driver):
    login = LoginPage(driver)
    login.login("", PASSWORD)

    assert "Username is required" in login.error_message()

def test_add_product_to_cart(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.wait_until_loaded() == "Products"
    inventory.add_backpack_to_cart()
    assert inventory.cart_count() == "1"
