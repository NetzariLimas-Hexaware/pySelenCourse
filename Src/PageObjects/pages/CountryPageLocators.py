from selenium.webdriver.common.by import By


class CountryPageLocators(object):
    select = dict(type=By.TAG_NAME, value="select")
    checkbox_agree = dict(type=By.CLASS_NAME, value="chkAgree")
    proceed = dict(type=By.XPATH, value="//button[contains(text(), 'Proceed')]")
