import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ViewCartPageLocators:
    labelShoppingCart = (By.CSS_SELECTOR, "div.breadcrumbs>ol>li.active")
    productOnShoppingCart = (By.CSS_SELECTOR, "td.cart_description>h4>a")
    btnProceedToCheckout = (By.CSS_SELECTOR, "#do_action div>a")







class ViewCartPage:

    def __init__(self, driver):
        self.driver = driver

    def getLabelShoppingCart(self):
        return self.driver.find_element(*ViewCartPageLocators.labelShoppingCart).text

    def getNameOfProductOnShoppingCart(self):
        return self.driver.find_element(*ViewCartPageLocators.productOnShoppingCart).text

    def seleccionarBtnProccedCheckout(self):
        self.driver.find_element(*ViewCartPageLocators.btnProceedToCheckout).click()

