import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--n2browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("n2browser_name")
    if browser_name == "chrome":
        s = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s = Service("C:\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    elif browser_name == "edge":
        s = Service("C:\\msedgedriver.exe")
        driver = webdriver.Edge(service=s)


    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

# implementation by Rahul Sheety - just copied
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# implementation by Rahul Sheety - just copied
def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

