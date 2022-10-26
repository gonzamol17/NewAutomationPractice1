import time
import pytest
import unittest
import sys
import os

from POM.CartPage import CartPage
from POM.ProductsPage import ProductsPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestLoadProductsToCart(BaseClass):

    def test_Load_Products_Cart(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        log.info("Se ingresa email y password")
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        hp.select_Products()
        pp = ProductsPage(driver)
        pp.selectWomenCategoryIcon()
        pp.selectDressWomenCategory()
        pp.addProductsToCart()
        hp.select_Cart()
        print("Se cargaron: "+str(pp.getQuantityLoadedDresses())+" Vestidos")




