import time
import pytest
import unittest
import sys
import os

from POM.ConfirmationPage import ConfirmationPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass
from POM.ProductsPage import ProductsPage
from POM.ViewCartPage import ViewCartPage
from POM.CartPage import CartPage
from POM.CheckoutPage import CheckoutPage
from POM.PaymentPage import PaymentPage


@pytest.mark.usefixtures("test_setup")
class TestMakeAPurchase(BaseClass):

    def test_Made_A_Purchase(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.select_SignIn()
        time.sleep(2)
        lp = LoginPage(driver)
        lp.do_Login("gonzalo.molina@darwoft.com", "Maestruli10")
        hp.select_Cart()
        cp = CartPage(driver)
        try:
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN + "El carrito de compras está limpio de productos")
            hp.select_Products()

        except:
            cp.clean_List_Of_Products()
            # time.sleep(3)
            assert "Cart is empty!" == cp.getLeyendEmptyCart()
            print(Fore.GREEN + "El carrito de compras está limpio de productos")
            hp.select_Products()
        print("Realizar una nueva selección de un producto para comprar")
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        pp = ProductsPage(driver)
        pp.selectBlueTopProduct()
        time.sleep(2)
        pp.goShoppingCart()
        vc = ViewCartPage(driver)
        assert "Shopping Cart" == vc.getLabelShoppingCart()
        assert "Blue Top" == vc.getNameOfProductOnShoppingCart()
        vc.seleccionarBtnProccedCheckout()
        time.sleep(2)
        cp = CheckoutPage(driver)
        assert "Checkout" == cp.getLabelCheckoutSection()
        assert "Address Details" == cp.getLabelAddressDetail()
        assert "Review Your Order" == cp.getReviewOrder()
        assert vc.getNameOfProductOnShoppingCart() == cp.getProductName()
        assert "Rs. 500" == cp.getProductPrice()
        print("El producto mostrado en checkout page es: "+cp.getProductName())
        print("El precio mostrado en checkout page es: " + cp.getProductPrice())
        time.sleep(2)
        cp.completeTextAreaComments("I am available between 12 and 3pm. for delivery time. Thanks.")
        time.sleep(2)
        cp.selectPlaceOrderBtn()
        time.sleep(2)
        pyp = PaymentPage(driver)
        pyp.completeAllInformationOnPaymentPage("Pedro Arias", "2323-2223-2322-2323", "123", "02", "2022")
        time.sleep(3)
        cop = ConfirmationPage(driver)
        assert "ORDER PLACED!" == cop.getLabelOrderPlacedSection()
        print(cop.getMessageOfConfirmation())
        cop.selectDownloadInvoice()
        print("Se descargó la Invoice, del producto comprado")
        time.sleep(3)
        cop.selectContinue()
        time.sleep(3)
        assert "https://www.automationexercise.com/" == self.driver.current_url
        print("Estamos en la actual url: "+self.driver.current_url)




