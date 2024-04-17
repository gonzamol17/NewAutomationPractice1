import time
import pytest
import unittest
import sys
import os

from POM.CartPage import CartPage
from POM.CategoryWomenPage import CategoryWomenPage
from POM.ContactUsPage import ContactUsPage
from POM.ProductsPage import ProductsPage
from POM.TestCasePage import TestCasePage
from POM.ViewCartPage import ViewCartPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestClickHereFromCart(BaseClass):

    def test_Click_From_Cart(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(2)
        hp.select_Cart()
        time.sleep(2)
        cp = CartPage(driver)
        try:
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN + "El carrito de compras está limpio de productos")
            cp.selectHereHyperlink()

        except:
            print(Fore.RED + "La cantidad de Productos a eliminar del carrito es: " + str(cp.getNumberOfProductToDelete())+Fore.RESET)
            cp.clean_List_Of_Products()
            #time.sleep(3)
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN+"El carrito de compras está limpio de productos")
            cp.selectHereHyperlink()
        time.sleep(5)
        pp = ProductsPage(driver)
        pp.selectBlueTopProduct()
        time.sleep(2)
        pp.goShoppingCart()
        hp.select_Home()
        time.sleep(2)
        hp.select_Cart()
        vc = ViewCartPage(driver)
        assert "Shopping Cart" == vc.getLabelShoppingCart()
        assert "Blue Top" == vc.getNameOfProductOnShoppingCart()
        print("Estamos en la página de Shopping Cart y todavía está seleccionado el producto: "+vc.getNameOfProductOnShoppingCart())

