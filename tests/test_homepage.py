import time

import pytest
from pom.homepage_nav import HomePageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomePageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Links text'
        elements = homepage_nav.get_nav_links()
        for index in range(2):
            homepage_nav.get_nav_links()[index].click()
            homepage_nav.driver.delete_all_cookies()
            time.sleep(3)
