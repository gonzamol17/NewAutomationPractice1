import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HomePageLocators:
    signInlink = (By.CSS_SELECTOR, "#header ul>li:nth-child(4)>a")
    logoutLink = (By.CSS_SELECTOR, "div.col-sm-8>div>ul>li:nth-child(4)>a")
    loggedLink = (By.CSS_SELECTOR, "li:nth-child(9)>a")
    footerSubscriptionTitle = (By.CSS_SELECTOR, "div.col-sm-3.col-sm-offset-1>div>h2")
    footerSubscriptionSubtitle = (By.CSS_SELECTOR, "div>form>p")
    alertSubscriptionSuccess = (By.CSS_SELECTOR, "#success-subscribe>div")
    boxSubscription = (By.ID, "susbscribe_email")
    btnSubscription = (By.ID, "subscribe")
    productsLink = (By.CSS_SELECTOR, "#header ul>li:nth-child(2)>a")
    brandProductsList = (By.CSS_SELECTOR, "div.brands_products>div>ul>li")
    brandsTitle = (By.CSS_SELECTOR, "div.brands_products>h2")
    contactUsLink = (By.CSS_SELECTOR, "div.col-sm-8>div>ul>li:nth-child(7)>a")
    categoryWomenLink = (By.CSS_SELECTOR, "div:nth-child(1)>div.panel-heading>h4>a>span>i")
    categoryWomenTopsLink = (By.CSS_SELECTOR, "#Women>div>ul>li:nth-child(2)>a")
    sliderWithPriceAndProduct = (By.CSS_SELECTOR, "div:nth-child(3)>div>div.single-products>div.product-overlay>div")
    cartLink = (By.CSS_SELECTOR, "li:nth-child(3)>a")
    homeLink = (By.CSS_SELECTOR, "ul>li:nth-child(1)>a")
    searchBox = (By.XPATH, "//input[@id='search_product']")
    glassSearch = (By.XPATH, "//button[@id='submit_search']")
    loggedInUser = (By.CSS_SELECTOR, "li:nth-child(9)>a")
    recommendedItems = (By.CSS_SELECTOR, "div.recommended_items>h2")
    numberRecommendedItems = (By.CSS_SELECTOR, "div.recommended_items div.productinfo.text-center>img:nth-child(1)")
    namesRecommendedItems1 = (By.XPATH, "//div[@id='recommended-item-carousel']/div/div[2]/div[3]/div/div/div/p")
    namesRecommendedItems2 = (By.XPATH, "")
    rightArrowItem = (By.CSS_SELECTOR, " a.right.recommended-item-control>i")
    testCaseLink = (By.CSS_SELECTOR, "#header li:nth-child(5)>a")
    apiTestingLink = (By.CSS_SELECTOR, "#header li:nth-child(6)>a")
    testCaseLinkLogin = (By.CSS_SELECTOR, "#header li:nth-child(6)>a")
    apiTestingLinkLogin = (By.CSS_SELECTOR, "#header li:nth-child(7)>a")


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def select_SignIn(self):
        self.driver.find_element(*HomePageLocators.signInlink).click()

    def select_Logout(self):
        self.driver.find_element(*HomePageLocators.logoutLink).click()

    def verify_Logged(self):
        return self.driver.find_element(*HomePageLocators.loggedLink).text

    def show_FooterTitle(self):
        return self.driver.find_element(*HomePageLocators.footerSubscriptionTitle).text

    def show_FooterSubTitle(self):
        return self.driver.find_element(*HomePageLocators.footerSubscriptionSubtitle).text

    def show_Alert_SubscriptionSuccess(self):
        return self.driver.find_element(*HomePageLocators.alertSubscriptionSuccess).text

    def sendEmailBoxSubscription(self, email):
        self.driver.find_element(*HomePageLocators.boxSubscription).send_keys(email)
        self.driver.find_element(*HomePageLocators.btnSubscription).click()


    def select_Products(self):
        self.driver.find_element(*HomePageLocators.productsLink).click()

    def scrollDownUntilBrandProducts(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*HomePageLocators.brandsTitle))
        hover.perform()

    def getAllBrandProducts(self):
        return self.driver.find_elements(*HomePageLocators.brandProductsList)


    def select_ContactUs(self):
        self.driver.find_element(*HomePageLocators.contactUsLink).click()


    def selectCategoryWomen(self):
        self.driver.find_element(*HomePageLocators.categoryWomenLink).click()


    def selectCategoryWomenTops(self):
        self.driver.find_element(*HomePageLocators.categoryWomenTopsLink).click()

    def verifyLoggedOut(self):
        return self.driver.find_element(*HomePageLocators.signInlink)

    def select_Cart(self):
        self.driver.find_element(*HomePageLocators.cartLink).click()

    def select_Home(self):
        self.driver.find_element(*HomePageLocators.homeLink).click()

    def selectSearchBox(self, product):
        self.driver.find_element(*HomePageLocators.searchBox).send_keys(product)
        time.sleep(2)
        self.driver.find_element(*HomePageLocators.glassSearch).click()
        time.sleep(2)


    def selectLoggedInUser(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*HomePageLocators.loggedInUser))
        hover.perform()

    def getLoggedInUserIcon(self):
        return self.driver.find_element(*HomePageLocators.loggedInUser)

    def getRecommededItemTitle(self):
        return self.driver.find_element(*HomePageLocators.recommendedItems).text

    def getAllRecommendedItems(self):
        return self.driver.find_elements(*HomePageLocators.numberRecommendedItems)

    def getNameRecommendedItems1(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, "#recommended-item-carousel>div>div.item.active>div:nth-child("+str(num)+")>div>div>div>p")

    def selectNextItem(self):
        self.driver.find_element(*HomePageLocators.rightArrowItem).click()


    def selectTestCaseLink(self):
        self.driver.find_element(*HomePageLocators.testCaseLink).click()


    def selectApisTestLink(self):
        self.driver.find_element(*HomePageLocators.apiTestingLink).click()

    def selectNewTabs(self):
        self.driver.find_element(*HomePageLocators.productsLink).send_keys(Keys.CONTROL + Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(*HomePageLocators.cartLink).send_keys(Keys.CONTROL + Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(*HomePageLocators.contactUsLink).send_keys(Keys.CONTROL + Keys.RETURN)


    def selectTestCaseLinkNewWindow(self):
        self.driver.find_element(*HomePageLocators.testCaseLinkLogin).send_keys(Keys.CONTROL + Keys.RETURN)


    def selectApisTestLinkNewWindow(self):
        self.driver.find_element(*HomePageLocators.apiTestingLinkLogin).send_keys(Keys.CONTROL + Keys.RETURN)
