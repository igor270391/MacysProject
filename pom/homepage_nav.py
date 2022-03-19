from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.selenium_base import SeleniumBase
from base.utils import Utils


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links = "#mainNavigationFobs>li"
        self.NAV_LINK_TEXT = "Women,Men,Kids & Baby,Home,Shoes,Handbags & Accessories,Jewelry,Sale"

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation links')

    def get_nav_links_text(self):
        nav_links = self.get_nav_links()
        nav_link_text = self.get_text_from_web_elements(nav_links)
        return Utils.join_string(nav_link_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
