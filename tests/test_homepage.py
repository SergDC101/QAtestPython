import time

import pytest
from pom.homepage_nav import HomePageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomePageNav(self.driver)
        # cookies = homepage_nav.driver.get_cookies()
        # cookies_name = [cookie['name'] for cookie in cookies]
        # print(cookies_name)
        for index in range(2):
            homepage_nav.get_nav_links()[index].click()

            time.sleep(3)
