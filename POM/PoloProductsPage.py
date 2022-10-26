from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PoloProductsPageLocators:
    titleBrandsPolo = (By.CSS_SELECTOR, "div.col-sm-9.padding-right>div>h2")
    quatityPoloProducts = (By.CSS_SELECTOR, "div>div>div.choose>ul>li>a")



class PoloProductsPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleBrandsPolo(self):
        return self.driver.find_element(*PoloProductsPageLocators.titleBrandsPolo).text

    def showTotalPoloProducts(self):
        return self.driver.find_elements(*PoloProductsPageLocators.quatityPoloProducts)
