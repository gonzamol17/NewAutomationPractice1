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


class TestWriteReview(BaseClass):

    def test_Write_Your_Review(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.select_SignIn()
        lp = LoginPage(driver)
        log.info("Se ingresa email y password")
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        assert "Logged in as" in hp.verify_Logged()
        self.driver.execute_script("window.scrollTo(0, 300)")
        hp.selectCategoryWomen()
        hp.selectCategoryWomenTops()
        cwp = CategoryWomenPage(driver)
        self.driver.execute_script("window.scrollTo(0, 200)")
        cwp.selectViewProductLink()
        time.sleep(3)
        assert "WRITE YOUR REVIEW" == cwp.getLabelWriteReview()
        self.driver.execute_script("window.scrollTo(0, 400)")
        cwp.completeReview("Gonzalo", "gonzalo.molina@darwoft.com", "This is only a test, to try complete the flow")
        assert cwp.getBannerReviewSuccessful().is_displayed()
        assert "rgba(60, 118, 61, 1)" in cwp.getBannerReviewSuccessful().value_of_css_property('color')
        print("Se pudo enviar correctamente la review del producto y se visualiza el mensaje verde: "+cwp.getTitleOfBannerReviewSuccessful())
        time.sleep(3)
