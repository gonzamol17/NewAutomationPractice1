import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM.ProductsPage import ProductsPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage


class TestHoverColorOneProduct(BaseClass):

    def test_HoverColorOneProduct(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_Products()
        time.sleep(3)
        pp = ProductsPage(driver)
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)
        assert pp.verify_SearchBox().is_displayed()
        time.sleep(3)
        print("\n")
        print("Como se está mostrando el box de búsqueda, estamos en la página de Productos")
        pp.select_MenTshirtProduct()
        time.sleep(3)
        assert 'rgba(254, 152, 15, 1)' in pp.show_HoverMenTshirtProduct().value_of_css_property('background-color')
        print("Se está visualizando un color naranja al hacer hover sobre el producto: "+pp.show_Title_TshirtBox())
        time.sleep(3)
