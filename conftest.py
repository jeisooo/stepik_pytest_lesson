import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', \
                        default="chrome",\
                        help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', \
                        default="ru",\
                        help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    
    

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        #browser = webdriver.Chrome()
        # присваиваем опции браузеру для скрытия
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        #options.binary_location = '/usr/bin/google-chrome-unstable'
        #options.add_argument('headless')
        #options.add_argument('window-size=1200x600')
        browser = webdriver.Chrome(options=options)
        # конец присваивания

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
