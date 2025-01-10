from Src.PageObjects.pages.ListingPageLocators import ListingPageLocators


class ListingPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.search_input = driver.find_element(ListingPageLocators.search_input.get("type"),
                                                ListingPageLocators.search_input.get("value"))

        self.addToCart = driver.find_element(ListingPageLocators.add_to_cart.get("type"),
                                             ListingPageLocators.add_to_cart.get("value"))

        self.openCart = driver.find_element(ListingPageLocators.cart_icon.get("type"),
                                            ListingPageLocators.cart_icon.get("value"))

        self.goToCheckout = driver.find_element(ListingPageLocators.go_to_checkout.get("type"),
                                                ListingPageLocators.go_to_checkout.get("value"))

    def get_search_input(self):
        return self.search_input

    def get_add_to_cart(self):
        return self.addToCart

    def get_cart_icon(self):
        return self.openCart

    def get_go_to_checkout(self):
        return self.goToCheckout
