import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM.ProductsPage import ProductsPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup")
class TestCountBrandProducts:

    def test_Count_Brands_Products(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 600)")
        #hp.scrollDownUntilBrandProducts()
        time.sleep(3)
        products = hp.getAllBrandProducts()
        print("\n")
        print("La Cantidad total de Brands mostradas es: "+str(len(hp.getAllBrandProducts())))
        print("Estos son las Cantidades Disponibles para cada Brand:")
        for i in products:
            print(i.text)

