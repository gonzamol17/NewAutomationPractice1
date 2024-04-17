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
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestListOfTestCases(BaseClass):

    def test_TestCases_List(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.selectTestCaseLink()
        time.sleep(2)
        tc = TestCasePage(driver)
        total = len(tc.getAllTestCases())
        total = total-1
        assert "TEST CASES" == tc.getTitleTestCase()
        print("Estamos en la sección de Test Cases")
        print("La cantidad de test cases listados es: "+str(total))
        aux = tc.getAllTestCases()
        n = 1
        print("El nombre de los Test Cases listados es:")
        for i in aux:
            if n != 27:
               print(i.text)
               n = n+1
            else:
                print("Eso fue todo, muchas gracias")


