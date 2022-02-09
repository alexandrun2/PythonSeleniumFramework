from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    #SHOP
    #  self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # let code know that should handle with an tuple
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    ## FORM
    # self.driver.find_element(By.NAME, "name").send_keys("Alexandru")  # filling input box with a value
    name = (By.NAME, "name")

    # self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("alex@alex.com")
    email = (By.CSS_SELECTOR, "input[name='email']")

    password = (By.ID, "exampleInputPassword1")

    # self.driver.find_element(By.ID, "exampleCheck1").click()  # checking a check box
    cakecheckbox = (By.ID, "exampleCheck1")

    # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    submit = (By.XPATH, "//input[@type='submit']")

    # self.driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").text
    successSumbit = (By.XPATH, "//div[contains(@class,'alert-success')]")

    # dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
    sexDropDown = (By.ID, "exampleFormControlSelect1")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getPaassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckCake(self):
        return self.driver.find_element(*HomePage.cakecheckbox)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def GetSuccessSubmit(self):
        return self.driver.find_element(*HomePage.successSumbit)

    def getGenderDrop(self):
        return self.driver.find_element(*HomePage.sexDropDown)

