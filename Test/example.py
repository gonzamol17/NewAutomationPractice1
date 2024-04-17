import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time



class TestVerify_Testimonials(BaseClass):


    def test_Verify_Testimonials(self):
        driver = self.driver
