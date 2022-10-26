from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CategoryWomenPageLocators:
    sliderPrice = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]")
    viewProductLink = (By.CSS_SELECTOR, "div:nth-child(3)>div>div.choose>ul>li>a")
    productNameBlueTop = (By.CSS_SELECTOR, "div.col-sm-7>div>h2")
    priceOfBlueTop = (By.CSS_SELECTOR, "div.col-sm-7>div>span>span")
    labelOfStock = (By.CSS_SELECTOR, "div.col-sm-7>div>p:nth-child(6)")
    labelWriteReview = (By.CSS_SELECTOR, "div.col-sm-12>ul>li>a")
    txtName = (By.ID, "name")
    txtEmail = (By.ID, "email")
    txtReview = (By.ID, "review")
    btnSubmit = (By.ID, "button-review")
    bannerReviewSuccessful = (By.CSS_SELECTOR, "#review-section>div>div>span")

class CategoryWomenPage:

    def __init__(self, driver):
        self.driver = driver

    def getPriceFromSlider(self):
        return self.driver.find_element(*CategoryWomenPageLocators.sliderPrice).text

    def selectViewProductLink(self):
        self.driver.find_element(*CategoryWomenPageLocators.viewProductLink).click()

    def getProductNameBlueTop(self):
        return self.driver.find_element(*CategoryWomenPageLocators.productNameBlueTop).text

    def getPriceBlueTop(self):
        return self.driver.find_element(*CategoryWomenPageLocators.priceOfBlueTop).text

    def getLabelWithStock(self):
        return self.driver.find_element(*CategoryWomenPageLocators.labelOfStock).text

    def getLabelWriteReview(self):
        return self.driver.find_element(*CategoryWomenPageLocators.labelWriteReview).text

    def completeReview(self, name, email, review):
        self.driver.find_element(*CategoryWomenPageLocators.txtName).send_keys(name)
        self.driver.find_element(*CategoryWomenPageLocators.txtEmail).send_keys(email)
        self.driver.find_element(*CategoryWomenPageLocators.txtReview).send_keys(review)
        self.driver.find_element(*CategoryWomenPageLocators.btnSubmit).click()

    def getBannerReviewSuccessful(self):
        return self.driver.find_element(*CategoryWomenPageLocators.bannerReviewSuccessful)

    def getTitleOfBannerReviewSuccessful(self):
        return self.driver.find_element(*CategoryWomenPageLocators.bannerReviewSuccessful).text



