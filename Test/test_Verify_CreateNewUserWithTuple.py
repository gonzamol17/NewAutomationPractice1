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
class TestCreateNewUser:

    def test_CreateNewUser(self, getData):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        lp = LoginPage(driver)
        time.sleep(3)
        lp.create_NewUser("Nielsen", "Nielse.Molina@hotmail.com")
        time.sleep(3)
        rp = RegistrationPage(driver)
        rp.complete_FormNewUser(getData[0], getData[1], getData[2], getData[3], getData[4], getData[5], getData[6],
                               getData[7], getData[8], getData[9], getData[10], getData[11], getData[12])
        assert "ACCOUNT CREATED!" == rp.verify_AccountCreatedSuccessfully()
        rp.select_BtnContinue()
        time.sleep(3)
        print("Se creó exitosamente la cuenta del usuario "+getData[5]+" "+getData[6])






    @pytest.fixture(params=[("Mr", "Maestruli10", "17", "May", "1979", "Nielsen", "Molina", "Luna 17",
                             "Australia", "Cordoba", "Cordoba", "4354", "324323424")])
    def getData(self, request):
        return request.param
