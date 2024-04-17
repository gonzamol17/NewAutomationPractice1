import time
import pytest
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestOpenNewTabs(BaseClass):

    def test_Open_NewTabs(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(3)
        hp.selectNewTabs()
        time.sleep(3)
        windows = driver.window_handles
        print("Los Id's de las ventanas abiertas son: " + str(windows))
        long = len(windows)
        print("La cantidad de ventanas abiertas es: " + str(long))
        time.sleep(3)
        aux = 3
        #"https://www.automationexercise.com/",
        #cree esta lista con las 4 url de las tabs que deberían abrirse, y la voy a usar para verificar
        #que las tabs abiertas correspondan a la url que tiene que abrirse y no otra
        lista = ["https://www.automationexercise.com/", "https://www.automationexercise.com/products", "https://www.automationexercise.com/view_cart", "https://www.automationexercise.com/contact_us"]
        try:
            for i in range(len(windows)):
                print("El título de la tab " + str(i+1) + " es: " + driver.title + " y la url es: " + driver.current_url)
            #Aca con el assert me estoy asegurando que el actual current url esté dentro de la lista que definí
            #para asegurarme que es una de las 4 tabs que me tiene que mostrar y no cualquier otra
                assert lista.__contains__(driver.current_url)
                driver.switch_to.window(windows[aux])
                aux = aux - 1
                time.sleep(2)
        except:
                print(Fore.RED + "Está faltando una url para comparar" + Fore.RESET)





