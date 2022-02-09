from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, ".card - title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # self.driver.find_element(By.CSS_SELECTOR, ".card-footer button")
    cardFooterAdd = (By.CSS_SELECTOR, ".card-footer button")
    # self.driver.find_element(By.XPATH, "//li[@class='nav-item active']/a")
    checkoutButton1 = (By.XPATH, "//li[@class='nav-item active']/a")
    # self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-success')]").click()
    checkoutButtonSuccess = (By.XPATH, "//button[contains(@class,'btn-success')]")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooterAdd(self):
        return self.driver.find_elements(*CheckoutPage.cardFooterAdd)

    def getcheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton1)

    def getcheckoutButtonSuccess(self):
        return self.driver.find_element(*CheckoutPage.checkoutButtonSuccess)

    def addToCardItem(self, itemtitles, productname):
        i = -1
        for card in itemtitles:
            i = i + 1
            cardText = card.text
            if cardText == productname:
                self.getCardFooterAdd()[i].click()




