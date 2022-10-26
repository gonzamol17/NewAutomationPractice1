import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ConfirmationPageLocators:
    labelOrderPlaced = (By.CSS_SELECTOR, "#form>div>div>div>h2>b")
    messageOfConfirmation = (By.CSS_SELECTOR, "#form>div>div>div>p")
    btnDownloadInvoice = (By.CSS_SELECTOR, "#form>div>div>div>a")
    btnContinue = (By.CSS_SELECTOR, "#form>div>div>div>div>a")


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    def getLabelOrderPlacedSection(self):
        return self.driver.find_element(*ConfirmationPageLocators.labelOrderPlaced).text

    def getMessageOfConfirmation(self):
        return self.driver.find_element(*ConfirmationPageLocators.messageOfConfirmation).text

    def selectDownloadInvoice(self):
        self.driver.find_element(*ConfirmationPageLocators.btnDownloadInvoice).click()

    def selectContinue(self):
        self.driver.find_element(*ConfirmationPageLocators.btnContinue).click()

