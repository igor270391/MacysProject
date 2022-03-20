import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from abstract.selenium_listiner import MyListener


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('chrome')  # use headless if you dont nee UI browser
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):  # "request" this is the fixture of pytest
    driver = get_webdriver
    driver = EventFiringWebDriver(driver, MyListener())  # we used to  delete cookie which blocks the page content
    url = "https://www.macys.com/"
    if request.cls is not None:  # in case we use driver(our test) in classes
        request.cls.driver = driver
    driver.get(url)  # in case we do not use inside the classes
    yield driver
    driver.quit()
