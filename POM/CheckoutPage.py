import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckoutPageLocators:
    labelCheckout = (By.CSS_SELECTOR, "div.breadcrumbs>ol>li.active")
    labelAddressDetails = (By.CSS_SELECTOR, "div:nth-child(2)>h2")
    labelReviewOrder = (By.CSS_SELECTOR, "div:nth-child(4)>h2")
    checkoutProductName = (By.CSS_SELECTOR, "td.cart_description>h4>a")
    checkoutProductPrice = (By.CSS_SELECTOR, "td:nth-child(4)>p")
    textAreaComments = (By.CSS_SELECTOR, "#ordermsg>textarea")
    btnPlaceOrder = (By.CSS_SELECTOR, "div:nth-child(7)>a")





class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def getLabelCheckoutSection(self):
        return self.driver.find_element(*CheckoutPageLocators.labelCheckout).text

    def getLabelAddressDetail(self):
        return self.driver.find_element(*CheckoutPageLocators.labelAddressDetails).text

    def getReviewOrder(self):
        return self.driver.find_element(*CheckoutPageLocators.labelReviewOrder).text

    def getProductName(self):
        return self.driver.find_element(*CheckoutPageLocators.checkoutProductName).text

    def getProductPrice(self):
        return self.driver.find_element(*CheckoutPageLocators.checkoutProductPrice).text

    def completeTextAreaComments(self, comments):
        self.driver.find_element(*CheckoutPageLocators.textAreaComments).send_keys(comments)

    def selectPlaceOrderBtn(self):
        self.driver.find_element(*CheckoutPageLocators.btnPlaceOrder).click()
