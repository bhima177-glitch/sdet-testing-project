from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.product_names = page.locator('[data-test="inventory-item-name"]')
        self.product_prices = page.locator('[data-test="inventory-item-price"]')

    def expect_loaded(self):
        expect(self.title).to_have_text("Products")

    def add_backpack_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def open_cart(self):
        self.cart_link.click()
        self.page.wait_for_url("**/cart.html")

    def sort_products(self, option: str):
        """SauceDemo sort values: az, za, lohi, hilo."""
        valid_options = {"az", "za", "lohi", "hilo"}
        if option not in valid_options:
            raise ValueError(
                f"Unsupported sort option {option!r}; choose one of {sorted(valid_options)}"
            )
        self.sort_dropdown.select_option(option)

    def sort_by_name_az(self):
        self.sort_products("az")

    def sort_by_name_za(self):
        self.sort_products("za")

    def sort_by_price_low_high(self):
        self.sort_products("lohi")

    def sort_by_price_high_low(self):
        self.sort_products("hilo")

    def get_product_names(self):
        return self.product_names.all_text_contents()

    def get_product_prices(self):
        values = self.product_prices.all_text_contents()
        return [float(value.replace("$", "").strip()) for value in values]
