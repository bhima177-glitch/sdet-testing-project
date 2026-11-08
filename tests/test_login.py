from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_with_valid_credentials(page, app_url):
    login = LoginPage(page)
    login.open(app_url)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.expect_loaded()


def test_login_with_invalid_password(page, app_url):
    login = LoginPage(page)
    login.open(app_url)
    login.login("standard_user", "wrong_password")
    login.expect_error("Username and password do not match")


def test_login_with_empty_credentials(page, app_url):
    login = LoginPage(page)
    login.open(app_url)
    login.login("", "")
    login.expect_error("Username is required")
