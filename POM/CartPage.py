import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPageLocators:
    leyendEmptyCart = (By.CSS_SELECTOR, "#empty_cart>p>b")
    optionDeleteProducts = (By.CSS_SELECTOR, "td.cart_delete>a")
    recordsOfProducts = (By.CSS_SELECTOR, "#cart_info_table>tbody>tr")
    tableOfProducts = (By.CSS_SELECTOR, "#cart_info_table>tbody")
    deleteProducts = (By.CSS_SELECTOR, " td.cart_delete>a")
    hereHiperlink = (By.CSS_SELECTOR, "#empty_cart>p>a>u")







class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def getLeyendEmptyCart(self):
        return self.driver.find_element(*CartPageLocators.leyendEmptyCart).text

    def getNumberOfProductToDelete(self):
        rows = len(self.driver.find_elements(*CartPageLocators.optionDeleteProducts))
        return rows

    def clean_List_Of_Products(self):
        #Esto es usando listas
        elements = len(self.driver.find_elements(*CartPageLocators.recordsOfProducts))
        ele = self.driver.find_elements(*CartPageLocators.tableOfProducts)
        for ele in range(1, elements+1):
            self.driver.find_element(*CartPageLocators.deleteProducts).click()
            time.sleep(3)


    def selectHereHyperlink(self):
        self.driver.find_element(*CartPageLocators.hereHiperlink).click()
