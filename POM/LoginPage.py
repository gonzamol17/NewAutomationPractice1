import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPageLocators:
    boxEmail = (By.CSS_SELECTOR, " div.col-sm-4.col-sm-offset-1>div>form>input[type=email]:nth-child(2)")
    boxPassword = (By.CSS_SELECTOR, "input[type=password]:nth-child(3)")
    btnLogin = (By.CSS_SELECTOR, "div.col-sm-4.col-sm-offset-1>div>form>button")
    errorMesssage = (By.CSS_SELECTOR, "div.col-sm-4.col-sm-offset-1>div>form>p")
    labelLogin = (By.CSS_SELECTOR, "div.col-sm-4.col-sm-offset-1>div>h2")
    boxNameSignUp = (By.CSS_SELECTOR, "input[type=text]:nth-child(2)")
    boxEmailSignUp = (By.CSS_SELECTOR, "input[type=email]:nth-child(3)")
    btnSignUp = (By.CSS_SELECTOR, "div:nth-child(3) > div > form > button")
    mgeUserAlreadyExit = (By.CSS_SELECTOR, "div:nth-child(3)>div>form>p")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def do_Login(self, email, password):
        self.driver.find_element(*LoginPageLocators.boxEmail).click()
        self.driver.find_element(*LoginPageLocators.boxEmail).send_keys(email)
        self.driver.find_element(*LoginPageLocators.boxPassword).click()
        self.driver.find_element(*LoginPageLocators.boxPassword).send_keys(password)
        self.driver.find_element(*LoginPageLocators.btnLogin).click()

    def show_ErrorLogin1(self):
        return self.driver.find_element(*LoginPageLocators.errorMesssage).text

    def show_StillLoginPage(self):
        return self.driver.find_element(*LoginPageLocators.labelLogin).text

    def create_NewUser(self, name, email):
        self.driver.find_element(*LoginPageLocators.boxNameSignUp).send_keys(name)
        self.driver.find_element(*LoginPageLocators.boxEmailSignUp).send_keys(email)
        self.driver.find_element(*LoginPageLocators.btnSignUp).click()
        time.sleep(4)

    def error_NewUser_AlreadyExist(self):
        return self.driver.find_element(*LoginPageLocators.mgeUserAlreadyExit)



