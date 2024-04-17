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


class TestQuantityRecommendedItems(BaseClass):

    def test_Quantity_Recommended_Items(self):
        driver = self.driver
        hp = HomePage(driver)
        self.driver.execute_script("window.scrollTo(0, 7500)")
        time.sleep(3)
        print("Se está visualizando el label "+hp.getRecommededItemTitle())
        cantidad = len(hp.getAllRecommendedItems())
        names = hp.getAllRecommendedItems()
        print("La cantidad de items listado en Recommended Items es: "+str(cantidad))
        n = 1
        m = 1
        b = 1
        for i in names:

            if n <= 3:

              aux = hp.getNameRecommendedItems1(n).text
              print(aux)
              n = n+1


            else:
              hp.selectNextItem()
              time.sleep(2)
              aux1 = hp.getNameRecommendedItems1(m).text
              m = m+1
              print(aux1)








