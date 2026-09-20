import pytest

from src.config.config import Config
from playwright.sync_api import sync_playwright



def pytest_addoption(parser):
    parser.addoption("--env",action="store",default="qa")



@pytest.fixture(scope="session")
def config(request):
    environment=request.config.getoption("--env")
    return Config(environment)


@pytest.fixture(scope="session")
def playwright():
    pw= sync_playwright().start()
    yield pw
    pw.stop()
#Everything before yield is setup.
#Everything after yield is cleanup.


@pytest.fixture(scope="session")
def browser(playwright,config):
    browser_name=config.get_browser_name()
    headless=config.get_headless()
    # Dynamically gets the BrowserType property (chromium/firefox/webkit) based on the browser name from config.
    browser_type = getattr(playwright, browser_name)
    browser_type=getattr(playwright,browser_name)
    browser=browser_type.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture()
def browser_context(browser):
    context=browser.new_context()
    yield context
    context.close()



# Default timeout:
# Maximum time Playwright waits for normal actions such as locating,
# clicking, filling, or interacting with elements before timing out.
# This is a maximum wait, not a fixed delay.

# Navigation timeout:
# Maximum time Playwright waits for navigation operations such as page.goto()
# or navigation triggered by an action before timing out.
# Navigation gets a separate timeout because page loading can take longer
# than normal element interactions.
@pytest.fixture
def page(config,browser_context):
    page=browser_context.new_page()
    page.set_default_timeout(config.get_default_timeout())
    page.set_navigation_timeout(config.get_navigation_timeout())
    yield page
    page.close()



