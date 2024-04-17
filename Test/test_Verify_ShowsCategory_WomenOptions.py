import time
import pytest
import unittest
import sys
import os

from POM.ConfirmationPage import ConfirmationPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass
from POM.ProductsPage import ProductsPage
from POM.ViewCartPage import ViewCartPage
from POM.CartPage import CartPage
from POM.CheckoutPage import CheckoutPage
from POM.PaymentPage import PaymentPage


class TestShowsCategoryWomenOption(BaseClass):

    def test_Verify_ShowsCategory_WomenOptions(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        lp = LoginPage(driver)
        log.info("Se ingresa email y password")
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        assert "Logged in as" in hp.verify_Logged()
        self.driver.execute_script("window.scrollTo(0, 700)")
        hp.selectCategoryWomen()
        time.sleep(3)
        pp = ProductsPage(driver)
        total = len(pp.counterCategoryWomenProducts())
        print("El total de items dentro de la categoria de Women es: "+str(total))
        names = pp.counterCategoryWomenProducts()
        num = 1
        for i in names:
            aux = pp.showIndividualCategoryWomenItem(num)
            print("El nombre del item número " + str(num) + " es " + aux)
            num = num + 1
        time.sleep(3)
        