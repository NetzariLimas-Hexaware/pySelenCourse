import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Src.PageObjects.pages.ListingPage import ListingPage
from Src.PageObjects.pages.CheckOutPage import CheckOutPage
from Src.PageObjects.pages.CountryPage import CountryPage
from time import sleep
from selenium.webdriver.common.keys import Keys
from Src.utils import WebDriverUtil


class SubmitOrderTest(unittest.TestCase):
    def test_submit_order(self):
        options = webdriver.ChromeOptions()
        service = Service("C://chromedriver-win64//chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(15)

        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        listing_page = ListingPage(driver)
        search_input = listing_page.get_search_input().send_keys("Cucumber")
        add_to_cart = listing_page.get_add_to_cart().click()
        open_cart = listing_page.get_cart_icon().click()
        go_to_checkout = listing_page.get_go_to_checkout().click()

        checkout_page = CheckOutPage(driver)
        promo_code_input = checkout_page.get_promo_code_input().send_keys("rahulshettyacademy")
        promo_code_button = checkout_page.get_promo_code_button().click()
        sleep(6)
        place_order = checkout_page.get_place_order().click()

        country_page = CountryPage(driver)
        select = country_page.get_select().send_keys("Mexico", Keys.ENTER)
        checkbox_agree = country_page.get_checkbox_agree().click()
        proceed = country_page.get_proceed().click()

        sleep(3)
        driver.quit()
        driver.close()


if __name__ == '__main__':
    unittest.main()
