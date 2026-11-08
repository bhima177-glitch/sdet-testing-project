from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.locator(".cart_item")
        self.remove_backpack = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )
        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )

    def expect_backpack_present(self):
        backpack = self.cart_item.filter(
            has_text="Sauce Labs Backpack"
        )
        expect(backpack).to_have_count(1)

    def remove_backpack_from_cart(self):
        self.remove_backpack.click()

    def proceed_to_checkout(self):
        self.checkout_button.click()