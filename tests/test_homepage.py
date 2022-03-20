import time

import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures("setup")
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.is_present('css', '#top>#closeButton', 'Close pop up advertise').click()
        # homepage_nav.driver.delete_cookie('ak_bmsc')  # delete issue cookie
        # searching cookie
        # cookies = homepage_nav.driver.get_cookies()
        # cookies_names = [cookie['name'] for cookie in cookies]
        # print(cookies_names)
        for index in range(8):  # click on each navigation link but before we dalete issue cookie (see class 'MyListener')
            homepage_nav.get_nav_links()[index].click()
            # homepage_nav.driver.delete_cookie('ak_bmsc')

            ## we looking for cookie, which block the page and delete them
            # for cookie_name in cookies_names:
            #     homepage_nav.driver.delete_cookie(cookie_name)
            #     homepage_nav.driver.refresh()
            #     homepage_nav.is_visible('tag_name', 'h1', cookie_name)
            #     print(cookie_name)
            # time.sleep(1.5)
