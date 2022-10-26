import time
import pytest
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestOpenManyTabs_CloseWithOrder(BaseClass):

    def test_OpenManyTabs_CloseWithoutOrder(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(2)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        time.sleep(2)
        hp.selectTestCaseLinkNewWindow()
        time.sleep(2)
        hp.selectApisTestLinkNewWindow()
        time.sleep(3)
        windows = driver.window_handles
        long = len(windows)
        print("La cantidad de ventanas abiertas es: " + str(long))
        time.sleep(3)
        aux = 0
        for i in range(len(windows)):
            driver.switch_to.window(windows[aux])
            print("El título de la tab " + str(i + 1) + " es: " + driver.title + " y la url es: " + driver.current_url)
            aux = aux+1
            time.sleep(2)

        flag1 = 1
        flag2 = 3
        while flag1 <= 2:
            driver.switch_to.window(windows[flag1])
            assert driver.current_url == "https://www.automationexercise.com/api_list" or driver.current_url == "https://www.automationexercise.com/test_cases"
            print("La url de la tab número " + str(flag2) + " es: " + driver.current_url)
            print("y la tab número " + str(flag2) + " se está cerrando")
            flag1 = flag1+1
            flag2 = flag2-1
            time.sleep(2)
            driver.close()
        driver.switch_to.window(windows[0])
        assert "https://www.automationexercise.com/" == driver.current_url
        print("La url de la tab número 1 es: " + driver.current_url)
        print("y la tab número 1 queda abierta")
        time.sleep(2)








