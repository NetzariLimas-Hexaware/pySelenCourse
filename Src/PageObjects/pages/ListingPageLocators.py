from selenium.webdriver.common.by import By


class ListingPageLocators(object):
    search_input = dict(type=By.CLASS_NAME, value="search-keyword")
    add_to_cart = dict(type=By.CSS_SELECTOR, value=".product-action button")
    cart_icon = dict(type=By.CLASS_NAME, value="cart-icon")
    go_to_checkout = dict(type=By.CSS_SELECTOR, value=".action-block button")
