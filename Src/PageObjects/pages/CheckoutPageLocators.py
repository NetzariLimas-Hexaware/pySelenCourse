from selenium.webdriver.common.by import By


class CheckoutPageLocators(object):
    promo_code_input = dict(type=By.CLASS_NAME, value="promoCode")
    promo_code_button = dict(type=By.CLASS_NAME, value="promoBtn")
    place_order = dict(type=By.XPATH, value="//button[contains(text(), 'Place Order')]")
