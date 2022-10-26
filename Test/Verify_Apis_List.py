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
from POM.TestCasePage import TestCasePage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestListOfApis(BaseClass):

    def test_Apis_List(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.selectApisTestLink()
        time.sleep(2)
        tc = TestCasePage(driver)
        total = len(tc.getAllApisNamesTest())
        total = total-1
        assert "APIS LIST FOR PRACTICE" == tc.getTitleApisTest()
        print("Estamos en la sección de Apis Test")
        print("La cantidad de Apis listadas es: "+str(total))
        aux = tc.getAllTestCases()
        n = 1
        print("El nombre de las Apis listadas es:")
        for i in aux:
            if n != 15:
               print(i.text)
               n = n+1
            else:
                print("Eso fue todo, muchas gracias")
