import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage


class TestFooterComponent(BaseClass):

    def test_FooterComponent(self):
        driver = self.driver
        hp = HomePage(driver)
        self.driver.execute_script("window.scrollTo(0, 7800)")
        time.sleep(4)
        title = hp.show_FooterTitle()
        subtitle = hp.show_FooterSubTitle()
        print("\n")
        assert "SUBSCRIPTION" == title
        assert subtitle == "Get the most recent updates from\nour site and be updated your self..."
        print("Se está visualizando el título en el footer: "+title)
        print("\nY también se está visualizando el subtítulo en el footer:\n"+subtitle)