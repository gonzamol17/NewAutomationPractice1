import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM.CategoryWomenPage import CategoryWomenPage
from POM.ContactUsPage import ContactUsPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestPriceAndProduct(BaseClass):

    def test_Price_And_Product(self):
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
        self.driver.execute_script("window.scrollTo(0, 300)")
        hp.selectCategoryWomen()
        time.sleep(3)
        hp.selectCategoryWomenTops()
        time.sleep(3)
        cwp = CategoryWomenPage(driver)
        price = cwp.getPriceFromSlider()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(3)
        cwp.selectViewProductLink()
        time.sleep(3)
        assert cwp.getProductNameBlueTop() == "Blue Top"
        assert cwp.getPriceBlueTop() == price
        time.sleep(3)
        print("El producto y precio, mostrado en el slider, es el mismo que se visualiza en el detalle")
        assert "In Stock" in cwp.getLabelWithStock()
        print("Hay Stock del producto")
        hp.select_Logout()
        time.sleep(3)
        assert hp.verifyLoggedOut().is_displayed()
        print("El usuario está deslogueado")


