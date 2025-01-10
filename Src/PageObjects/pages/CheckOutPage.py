from Src.PageObjects.pages.CheckoutPageLocators import CheckoutPageLocators


class CheckOutPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.promo_code_input = driver.find_element(CheckoutPageLocators.promo_code_input.get("type"),
                                                    CheckoutPageLocators.promo_code_input.get("value"))

        self.promo_code_button = driver.find_element(CheckoutPageLocators.promo_code_button.get("type"),
                                                     CheckoutPageLocators.promo_code_button.get("value"))

        self.place_order = driver.find_element(CheckoutPageLocators.place_order.get("type"),
                                               CheckoutPageLocators.place_order.get("value"))

    def get_promo_code_input(self):
        return self.promo_code_input

    def get_promo_code_button(self):
        return self.promo_code_button

    def get_place_order(self):
        return self.place_order
