from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactUsPageLocators:
    getInTouch = (By.CSS_SELECTOR, "div.col-sm-8>div>h2")
    labelName = (By.CSS_SELECTOR, "div:nth-child(2)>input")
    labelEmail = (By.CSS_SELECTOR, "div:nth-child(3)>input")
    labelSubject = (By.CSS_SELECTOR, "div:nth-child(4)>input")
    txtboxMessage = (By.ID, "message")
    btnSubmit = (By.CSS_SELECTOR, "div:nth-child(7)>input")
    alertSuccess = (By.CSS_SELECTOR, "div.status.alert.alert-success")
    btnHome = (By.CSS_SELECTOR, "#form-section>a")





class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver


    def getTitleContactUsForm(self):
        return self.driver.find_element(*ContactUsPageLocators.getInTouch).text

    def completeForm(self, name, email, subject, text):
        self.driver.find_element(*ContactUsPageLocators.labelName).send_keys(name)
        self.driver.find_element(*ContactUsPageLocators.labelEmail).send_keys(email)
        self.driver.find_element(*ContactUsPageLocators.labelSubject).send_keys(subject)
        self.driver.find_element(*ContactUsPageLocators.txtboxMessage).send_keys(text)
        self.driver.find_element(*ContactUsPageLocators.btnSubmit).click()

    def getAlertSuccess(self):
        return self.driver.find_element(*ContactUsPageLocators.alertSuccess).text

    def selectBtnReturnHomePage(self):
        return self.driver.find_element(*ContactUsPageLocators.btnHome).click()