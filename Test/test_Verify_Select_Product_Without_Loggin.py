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


class TestSelectProductWithLoggin(BaseClass):

    def test_Select_Product_Without_Loggin(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(2)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        hp.select_Cart()
        cp = CartPage(driver)
        try:
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN + "El carrito de compras está limpio de productos")

        except:
            cp.clean_List_Of_Products()
            # time.sleep(3)
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN + "El carrito de compras está limpio de productos")

        time.sleep(2)
        hp.select_Logout()
        hp.select_Products()
        print("Realizar una selección de un producto sin estar logueado")
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        pp = ProductsPage(driver)
        pp.selectBlueTopProduct()
        print("Se agregó el producto seleccionado sin estar logueado")
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        # Logged in as
        assert "Logged in as" in hp.verify_Logged()
        print("El usuario está logueado")
        hp.select_Cart()
        vc = ViewCartPage(driver)
        assert "Shopping Cart" == vc.getLabelShoppingCart()
        assert "Blue Top" == vc.getNameOfProductOnShoppingCart()
        print("El producto elegido sin estar logueado, se sigue visualizando estando logueado")
