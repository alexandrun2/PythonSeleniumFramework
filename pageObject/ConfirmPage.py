from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "//input[@id='country']")
    addressInput = (By.XPATH, "//input[@id='country']")
    # self.driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")
    suggestedLocations = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    agreeCheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element(By.XPATH, "//input[contains(@class,'btn-success')]")
    purchaseButton = (By.XPATH, "//input[contains(@class,'btn-success')]")
    #self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    successOrderText = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def getAddressInput(self):
        return self.driver.find_element(*ConfirmPage.addressInput)

    def getsuggestedLocations(self):
        return self.driver.find_elements(*ConfirmPage.suggestedLocations)

    def getagreeCheckBox(self):
        return self.driver.find_element(*ConfirmPage.agreeCheckBox)

    def getpurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getsuccessOrderText(self):
        return self.driver.find_element(*ConfirmPage.successOrderText)

    def selectSuggestedLocation(self, suggestedLocations, location):
        i = -1
        for locations in suggestedLocations:
            i = i + 1
            if locations.text == location:
                suggestedLocations[i].click()


