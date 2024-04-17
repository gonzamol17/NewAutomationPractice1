import time
import pytest
import unittest
import sys
import os

from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils


class TestLoginSuccessWithJson(BaseClass):

    def test_LoginSuccessWithJson(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.select_SignIn()
        lp = LoginPage(driver)
        file = open("C:\\Users\\User\\PycharmProjects\\NewAutomationPractice1\\Data\\Login.json", "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        list = obj['users']
        for i in range(len(list)):
            email = list[i].get("email")
            password = list[i].get("password")
            lp.do_Login(email, password)
            assert "Logged in as" in hp.verify_Logged()
            print("El usuario "+email+" está logueado")
            time.sleep(3)
            hp.select_Logout()
            print("El usuario " + email + " ya está deslogueado")
            time.sleep(3)

