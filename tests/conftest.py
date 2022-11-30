import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# Установка параметров запуска Chrome
@pytest.fixture()
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    return options


# Инициализзация webdriver
@pytest.fixture()
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='ChromeDriver/chromedriver.exe', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.avito.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()
