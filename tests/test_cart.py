from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_product_and_verify_cart_badge(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    expect(inventory.cart_badge).to_have_text("1")


def test_product_is_visible_in_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    cart.expect_backpack_present()


def test_remove_product_from_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    cart.remove_backpack_from_cart()
    expect(cart.cart_item).to_have_count(0)
