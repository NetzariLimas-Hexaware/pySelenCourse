from Src.PageObjects.pages.CountryPageLocators import CountryPageLocators


class CountryPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.select = driver.find_element(CountryPageLocators.select.get("type"),
                                          CountryPageLocators.select.get("value"))

        self.checkbox_agree = driver.find_element(CountryPageLocators.checkbox_agree.get("type"),
                                                  CountryPageLocators.checkbox_agree.get("value"))

        self.proceed = driver.find_element(CountryPageLocators.proceed.get("type"),
                                           CountryPageLocators.proceed.get("value"))

    def get_select(self):
        return self.select

    def get_checkbox_agree(self):
        return self.checkbox_agree

    def get_proceed(self):
        return self.proceed
