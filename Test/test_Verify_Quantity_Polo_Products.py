import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM.PoloProductsPage import PoloProductsPage
from POM.ProductsPage import ProductsPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage


class TestQuantityPoloProducts(BaseClass):

    def test_Quantity_Polo_Products(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        assert "Logged in as" in hp.verify_Logged()
        time.sleep(3)
        hp.select_Products()
        time.sleep(3)
        pp = ProductsPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(3)
        number = pp.totalNumberBrandsPolo()
        print("\n")
        print("La cantidad de prendas y tipo es: "+number)
        pp.selectBrandsPolo()
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(3)
        ppp = PoloProductsPage(driver)
        assert ppp.showTitleBrandsPolo() == "BRAND - POLO PRODUCTS"
        total = len(ppp.showTotalPoloProducts())
        print("La cantidad total de productos Polo listados es: "+str(total))
        time.sleep(3)
        assert str(total) in str(number)
        print("Tanto en el summary de Brands-Polo como en la sección Polos existe la misma cantidad de "
              "productos y es: "+str(total))
