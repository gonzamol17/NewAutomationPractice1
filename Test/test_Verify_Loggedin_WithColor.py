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
class TestVerify_LoggedInUser(BaseClass):

    def test_LoggedIn_User(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        hp.select_Home()
        hp.selectLoggedInUser()
        time.sleep(3)
        assert "rgba(254, 152, 15, 1)" in hp.getLoggedInUserIcon().value_of_css_property('color')
        print("Se está visualizando el icono LoggedInUserName, con el color naranja")
