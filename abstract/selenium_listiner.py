from selenium.webdriver.support.events import AbstractEventListener

from base.selenium_base import SeleniumBase


class MyListener(AbstractEventListener):

    def before_click(self, element, driver):
        SeleniumBase(driver).delete_cookie_by_name('ak_bmsc')

    def after_click(self, element, driver):
        SeleniumBase(driver).delete_cookie_by_name('ak_bmsc')