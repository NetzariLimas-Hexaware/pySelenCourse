import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverUtil(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        service = Service("C://chromedriver-win64//chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
