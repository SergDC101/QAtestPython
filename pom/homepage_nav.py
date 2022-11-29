from base.seleniumBase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class HomePageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '.index-nav-r2kHM>li'
        self.NAV_LINK_TEXT = "Для бизнеса,Помощь"


    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')



    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text)
