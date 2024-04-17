import time
import pytest
import unittest
import sys
import os

from POM.CartPage import CartPage


sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestClean_Cart(BaseClass):

    def test_Clean_Cart(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        log.info("Se ingresa email y password")
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        assert "Logged in as" in hp.verify_Logged()
        hp.select_Cart()
        cp = CartPage(driver)
        try:
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN + "El carrito de compras está limpio de productos")
            hp.select_Home()

        except:
            print(Fore.RED + "La cantidad de Productos a eliminar del carrito es: " + str(cp.getNumberOfProductToDelete())+Fore.RESET)
            cp.clean_List_Of_Products()
            #time.sleep(3)
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN+"El carrito de compras está limpio de productos")
            hp.select_Home()


