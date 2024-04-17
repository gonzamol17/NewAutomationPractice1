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
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestSearch_Products(BaseClass):

    def test_Search_Products(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        hp.select_Products()
        product = "Unicorn Print"
        hp.selectSearchBox(product)
        try:
            self.driver.execute_script("window.scrollTo(0, 400)")
            pp = ProductsPage(driver)
            assert product in pp.verifyUnicornprintProduct()
            print(Fore.GREEN+"Se ha encontrado el producto buscado que es "+pp.verifyUnicornprintProduct()+Fore.RESET)
            time.sleep(2)
        except:
            print(Fore.RED + "El producto buscado no existe en la web"+Fore.RESET)


