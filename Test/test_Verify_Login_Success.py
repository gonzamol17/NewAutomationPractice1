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
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestLoginSuccess(BaseClass):

    def test_Login_Success(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        log.info("Se hace click en link signIn")
        hp.select_SignIn()
        time.sleep(3)
        lp = LoginPage(driver)
        log.info("Se ingresa email y password")
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        #Logged in as
        assert "Logged in as" in hp.verify_Logged()
        log.info("El usuario está logueado")
        time.sleep(3)
