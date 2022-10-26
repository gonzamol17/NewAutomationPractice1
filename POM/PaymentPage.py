import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PaymentPageLocators:
    labelPayment = (By.CSS_SELECTOR, "div.breadcrumbs>ol>li.active")
    cardNameBox = (By.CSS_SELECTOR, "div:nth-child(2)>div>input")
    cardNumberBox = (By.CSS_SELECTOR, "div:nth-child(3)>div>input")
    cvcCardBox = (By.CSS_SELECTOR, "div.col-sm-4.form-group.cvc>input")
    monthExpirationCardBox = (By.CSS_SELECTOR, "div:nth-child(2)>input")
    yearExpirationCardBox = (By.CSS_SELECTOR, "div:nth-child(3)>input")
    btnPayAndConfirm = (By.CSS_SELECTOR, "#submit")


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver

    def getLabelPaymentSection(self):
        return self.driver.find_element(*PaymentPageLocators.labelPayment).text

    def completeAllInformationOnPaymentPage(self, name, number, cvc, month, year):
        self.driver.find_element(*PaymentPageLocators.cardNameBox).send_keys(name)
        self.driver.find_element(*PaymentPageLocators.cardNumberBox).send_keys(number)
        self.driver.find_element(*PaymentPageLocators.cvcCardBox).send_keys(cvc)
        self.driver.find_element(*PaymentPageLocators.monthExpirationCardBox).send_keys(month)
        self.driver.find_element(*PaymentPageLocators.yearExpirationCardBox).send_keys(year)
        self.driver.find_element(*PaymentPageLocators.btnPayAndConfirm).click()



