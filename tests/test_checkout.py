from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    cart.expect_backpack_present()
    cart.proceed_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_customer_information("Bhima", "Sankar", "534211")
    checkout.finish_order()
    checkout.expect_order_complete()
