import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestCasePageLocators:
    namesTestCases = (By.CSS_SELECTOR, "#form div.panel-heading>h4")
    titleTestCase = (By.CSS_SELECTOR, "#form>div>div.row>div>h2>b")
    titleApisTest = (By.CSS_SELECTOR, "#form>div>div.row>div>h2>b")
    nameApisTest = (By.CSS_SELECTOR, "#form div.panel-heading>h4")



class TestCasePage:

    def __init__(self, driver):
        self.driver = driver

    def getAllTestCases(self):
        return self.driver.find_elements(*TestCasePageLocators.namesTestCases)

    def getAllNamesTestCases(self):
        return self.driver.find_elements(*TestCasePageLocators.namesTestCases)

    def getTitleTestCase(self):
        return self.driver.find_element(*TestCasePageLocators.titleTestCase).text

    def getTitleApisTest(self):
        return self.driver.find_element(*TestCasePageLocators.titleTestCase).text

    def getAllApisNamesTest(self):
        return self.driver.find_elements(*TestCasePageLocators.nameApisTest)
