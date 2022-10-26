import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM.RegistrationPage import RegistrationPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup")
class TestNewUser_AlreadyCreated:

    def test_NewUser_AlreadyCreated (self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        lp = LoginPage(driver)
        time.sleep(3)
        lp.create_NewUser("Nicolas", "Nicolas.Molina@hotmail.com")
        time.sleep(3)
        assert "Email Address already exist!" == lp.error_NewUser_AlreadyExist().text
        time.sleep(3)
        #rp = RegistrationPage(driver)
        #rp.complete_FormNewUser(getdata["gender"], getdata["password"], getdata["day"], getdata["month"],
        #                        getdata["year"], getdata["firstname"], getdata["lastname"],
        #                        getdata["address"], getdata["country"], getdata["state"], getdata["city"],
        #                        getdata["zip"], getdata["mobile"])

        assert 'rgba(255, 0, 0, 1)' in lp.error_NewUser_AlreadyExist().value_of_css_property('color')
        print("se visualiza el error en rojo: "+lp.error_NewUser_AlreadyExist().text)
        time.sleep(3)
