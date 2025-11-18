import time
import pytest
import unittest
import sys
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from POM.CartPage import CartPage
from POM.ProductsPage import ProductsPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestCountAllProducts(BaseClass):

    def test_CountAll_Products(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        self.driver.execute_script("window.scrollTo(0, 600)")
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        time.sleep(1)
        hp.select_Products()
        self.driver.execute_script("window.scrollTo(0, 600)")
        pp = ProductsPage(driver)
        time.sleep(2)
        total = len(pp.counterOfAllProducts())
        assert 34 == total
        names = pp.counterOfAllProducts()
        print("La cantidad total de productos listados es: "+str(total))
        num = 3

        for i in names:
            aux = pp.showIndividualName(num)
            print("El nombre del producto número "+str(num-2)+" es "+aux)
            num = num+1







