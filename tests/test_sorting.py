from pages.inventory_page import InventoryPage


def test_sort_products_name_az(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_name_az()
    names = inventory.get_product_names()
    assert names == sorted(names)


def test_sort_products_name_za(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_name_za()
    names = inventory.get_product_names()
    assert names == sorted(names, reverse=True)


def test_sort_products_price_low_high(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_price_low_high()
    prices = inventory.get_product_prices()
    assert prices == sorted(prices)


def test_sort_products_price_high_low(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_price_high_low()
    prices = inventory.get_product_prices()
    assert prices == sorted(prices, reverse=True)
