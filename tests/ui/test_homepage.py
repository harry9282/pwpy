from playwright.sync_api import Page
from src.config.config import Config
from src.pages.homepage import HomePage
import time


def test_heading_of_homepage(config:Config,page:Page):
    homepage= HomePage(page)
    current_title=homepage.title
    time.sleep(10)
    assert current_title in "WebDriverUniversity – Free Test Automation Practice Site (AI, Playwright, Selenium, Cypress"



