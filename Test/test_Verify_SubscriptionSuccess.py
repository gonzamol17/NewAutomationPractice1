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


class TestSubscriptionSuccess(BaseClass):

    def test_Subscription_Success(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        self.driver.execute_script("window.scrollTo(0, 7800)")
        time.sleep(3)
        hp.sendEmailBoxSubscription("gonzalo.molina@darwoft.com")
        text = hp.show_Alert_SubscriptionSuccess()
        assert text == "You have been successfully subscribed!"
        log.info("Se pudo enviar la subscripción exitosamente")
        print("Se pudo enviar la subscripción exitosamente")
        time.sleep(3)
