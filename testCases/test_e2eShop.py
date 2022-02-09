# all tests should be wrapped in a class
# browse invocation code should not be in test case -- should be generic
from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseTestClass import BaseTestClass


class TestOne(BaseTestClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        # homepage.shopItems().click() # moved to HomePage method - shopItems
        # checkoutPage = CheckoutPage(self.driver) # moved to HomePage method - shopItems
        checkoutPage = homepage.shopItems()
        log.info("Getting shop items/cards")
        cards = checkoutPage.getCardTitles()
        log.info("Getting shop items/cards titles")

        """
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == "Blackberry":
                checkoutPage.getCardFooterAdd()[i].click()
                log.info("Adding blackberry item in the cart")
        """
        checkoutPage.addToCardItem(cards, "Blackberry")
        log.info("Adding blackberry item in the cart")

        # click on cart
        checkoutPage.getcheckoutButton().click()
        log.info("Opening cart")

        # click on checkout
        checkoutPage.getcheckoutButtonSuccess().click()
        log.info("Clicking on checkout button")

        ## enter delivery location by suggestion starting from Ro string
        confirmPage = ConfirmPage(self.driver)
        inputAddress = confirmPage.getAddressInput()
        inputAddress.send_keys("Ro")

        # time.sleep(6) # wait to load suggested values
        # explicitWait = WebDriverWait(self.driver, 10)
        # explicitWait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Romania")))
        self.verifyLinkPresence("Romania")

        # select Romania from list
        suggestedLocations = confirmPage.getsuggestedLocations()

        """
        i = -1
        for locations in suggestedLocations:
            i = i + 1
            if locations.text == "Romania":
                suggestedLocations[i].click()
                log.info("Selecting delivery location")
        """
        confirmPage.selectSuggestedLocation(suggestedLocations, "Romania")
        log.info("Selecting delivery location")

        # check "I agree with the term & Conditions" checkbox
        confirmPage.getagreeCheckBox().click()

        # click on Purchase
        confirmPage.getpurchaseButton().click()
        log.info("Proceed with finish sale operation..")

        # checking if success alert is displayed
        n2SuccessOrderMSg = confirmPage.getsuccessOrderText().text
        print(n2SuccessOrderMSg)

        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in n2SuccessOrderMSg
        log.info("Order placed successfully")