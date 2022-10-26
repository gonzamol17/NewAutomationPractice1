import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
import HtmlTestRunner


@pytest.mark.usefixtures("test_setup")
class TestVerify_Testimonials():


    def test_Verify_Testimonials(self):
        driver = self.driver
