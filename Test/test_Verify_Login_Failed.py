import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup")
class TestLoginFailed:

    def test_Login_Failed(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli11")
        time.sleep(3)
        error = 'Your email or password is incorrect!'
        assert error == lp.show_ErrorLogin1()


    def test_Login_Failed_WithoutEmail(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        lp.do_Login("", "Maestruli10")
        time.sleep(3)
        labelLogin = 'Login to your account'
        assert labelLogin == lp.show_StillLoginPage()
        print("Debes completar el Email")

    def test_Login_Failed_WithoutPass(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "")
        time.sleep(3)
        labelLogin = 'Login to your account'
        assert labelLogin == lp.show_StillLoginPage()
        print("Debes completar la contraseña")
