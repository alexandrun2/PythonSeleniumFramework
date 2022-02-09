import time

import pytest

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseTestClass import BaseTestClass


class TestHomePage(BaseTestClass):

    def test_FormSubmission(self, getTestData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getTestData["firstName"])
        log.info("entering firstName: " + getTestData["firstName"])
        homePage.getemail().send_keys(getTestData["mail"])
        log.info("entering mail: " + getTestData["mail"])
        homePage.getPaassword().send_keys(getTestData["pass"])
        log.info("entering pass: " + getTestData["pass"])
        homePage.getCheckCake().click()
        homePage.getSubmit().click()
        self.selectOptionByText(homePage.getGenderDrop(), (getTestData["gender"]))
        log.info("selecting gender: " + getTestData["gender"])

        message = homePage.GetSuccessSubmit().text
        assert "Success! The Form has been submitted successfully!." in message  # to check if PASS
        log.info("Done: " + message)

        time.sleep(2)
        self.driver.refresh() #  in order to refresh page after each data set used for testing

    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    # @pytest.fixture(params=HomePageData.getTestDataExcel("Testcase1"))
    @pytest.fixture(params=HomePageData.getTestAllDataExcel())
    def getTestData(self, request):
        return request.param
