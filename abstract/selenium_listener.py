from lib2to3.pgen2 import driver

from selenium.webdriver.support.events import AbstractEventListener
from base.seleniumBase import SeleniumBase


class MyListener(AbstractEventListener):

    def before_click(self, element, driver):
        SeleniumBase(driver).delete_cookie('ut')

    def after_click(self, element, driver):
        SeleniumBase(driver).delete_cookie('ut')