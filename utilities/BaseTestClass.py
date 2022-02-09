import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseTestClass:

    def verifyLinkPresence(self, text):
        explicitWait = WebDriverWait(self.driver, 10)
        explicitWait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        # n2logger = logging.getLogger(__name__)  # capture automatically test file name using param __name__
        n2logger = logging.getLogger(loggerName)
        n2fileHandler = logging.FileHandler("logFile.log")
        n2formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        n2fileHandler.setFormatter(n2formatter)
        n2logger.addHandler(n2fileHandler)  # filehandler object
        n2logger.setLevel(logging.DEBUG)
        return n2logger