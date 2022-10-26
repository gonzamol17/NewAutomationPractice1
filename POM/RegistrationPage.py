import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class RegistrationPageLocators():
    signInlink = (By.CSS_SELECTOR, "#header>div>div>div>div.col-sm-8>div>ul>li:nth-child(4)>a")
    passwordRegistration = (By.ID, "password")
    dropdownDays = (By.ID, "days")
    dropdownMonths = (By.ID, "months")
    dropdownYears = (By.ID, "years")
    firstName =(By.ID, "first_name")
    lastName = (By.ID, "last_name")
    newAddress = (By.ID, "address1")
    dropdownCo = (By.ID, "country")
    newState = (By.ID, "state")
    newCity = (By.ID, "city")
    newZipCode = (By.ID, "zipcode")
    newMobileNumber = (By.ID, "mobile_number")
    btnCreateAccount = (By.CSS_SELECTOR, "#form>div>div>div>div>form>button")
    radioButtonGender = (By.ID, "uniform-id_gender1")
    radioButtonMr = (By.ID, "id_gender1")
    radioButtonMrs = (By.ID, "id_gender2")
    txtAccountCreated = (By.CSS_SELECTOR, "#form>div>div>div>h2")
    btnContinue = (By.CSS_SELECTOR, "#form>div>div>div>div>a")

class RegistrationPage():

    def __init__(self, driver):
        self.driver = driver


    def complete_FormNewUser(self, gender, password, day, month, year, name, lastname, address, country, state, city, zip, mobile):
        if gender == "Mr":
            self.driver.find_element(*RegistrationPageLocators.radioButtonMr).click()
        else:
            self.driver.find_element(*RegistrationPageLocators.radioButtonMrs).click()
        self.driver.find_element(*RegistrationPageLocators.passwordRegistration).send_keys(password)
        self.driver.execute_script("window.scrollTo(0, 300)")
        sel = Select(self.driver.find_element(*RegistrationPageLocators.dropdownDays))
        sel.select_by_visible_text(day)
        sel = Select(self.driver.find_element(*RegistrationPageLocators.dropdownMonths))
        sel.select_by_visible_text(month)
        sel = Select(self.driver.find_element(*RegistrationPageLocators.dropdownYears))
        sel.select_by_visible_text(year)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element(*RegistrationPageLocators.firstName).send_keys(name)
        self.driver.find_element(*RegistrationPageLocators.lastName).send_keys(lastname)
        self.driver.find_element(*RegistrationPageLocators.newAddress).send_keys(address)
        self.driver.execute_script("window.scrollTo(0, 300)")
        sel = Select(self.driver.find_element(*RegistrationPageLocators.dropdownCo))
        sel.select_by_visible_text(country)
        self.driver.find_element(*RegistrationPageLocators.newState).send_keys(state)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element(*RegistrationPageLocators.newCity).send_keys(city)
        self.driver.find_element(*RegistrationPageLocators.newZipCode).send_keys(zip)
        self.driver.find_element(*RegistrationPageLocators.newMobileNumber).send_keys(mobile)
        self.driver.find_element(*RegistrationPageLocators.btnCreateAccount).click()
        time.sleep(5)


    def verify_AccountCreatedSuccessfully(self):
        return self.driver.find_element(*RegistrationPageLocators.txtAccountCreated).text

    def select_BtnContinue(self):
        self.driver.find_element(*RegistrationPageLocators.btnContinue).click()
