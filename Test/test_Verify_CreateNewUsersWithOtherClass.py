import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM.RegistrationPage import RegistrationPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Data.DataNewUsersPage import DataNewUsersPage


class TestCreateNewUserWithOtherClass(BaseClass):

    def test_CreateNewUserWhitOtherclass (self, getdata):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        lp = LoginPage(driver)
        time.sleep(3)
        lp.create_NewUser("Lucas", "Lucas.Molina@hotmail.com")
        time.sleep(3)
        rp = RegistrationPage(driver)
        rp.complete_FormNewUser(getdata["gender"], getdata["password"], getdata["day"], getdata["month"],
                                getdata["year"], getdata["firstname"], getdata["lastname"],
                                getdata["address"], getdata["country"], getdata["state"], getdata["city"],
                                getdata["zip"], getdata["mobile"])
        assert "ACCOUNT CREATED!" == rp.verify_AccountCreatedSuccessfully()
        rp.select_BtnContinue()
        time.sleep(3)
        print("Se creó exitosamente la cuenta del usuario " + getdata["firstname"]+" "+getdata["lastname"])






    @pytest.fixture(params=DataNewUsersPage.test_DataOfNewUsers)
    def getdata(self, request):
        return request.param
