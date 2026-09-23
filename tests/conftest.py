
from pathlib import Path
import re

import pytest
import os
from pytest import Item
from pytest import TestReport
from pytest import CallInfo
from src.config.config import Config
from pages.home_page import HomePage
from playwright.sync_api import BrowserType, sync_playwright
from playwright.sync_api import Playwright, Page,BrowserContext, Browser

from src.utils.evidence_manager import EvidenceManager


def pytest_addoption(parser):
    parser.addoption("--env",action="store",default="qa")

@pytest.fixture(scope="session")
def config(request):
    environment:str=request.config.getoption("--env")
    return Config(environment)

@pytest.fixture(scope="session")
def playwright() :
    pw:Playwright = sync_playwright().start()
    yield pw
    pw.stop()
#Everything before yield is setup.
#Everything after yield is cleanup.

@pytest.fixture(scope="session")
def browser(playwright:Playwright,config:Config):
    browser_name:str=config.get_browser_name()
    headless:bool=config.get_headless()
    # Dynamically gets the BrowserType property (chromium/firefox/webkit) based on the browser name from config.
    browser_type:BrowserType = getattr(playwright, browser_name)
    browser:Browser=browser_type.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture()
def browser_context(browser:Browser,config:Config):
    storage_state_path=Path("state") / config.environment / "state.json"
    if not storage_state_path.exists():
        context: BrowserContext=browser.new_context(record_video_dir="./videos")
        context.tracing.start(screenshots=True,snapshots=True,sources=True)
    else:
        context: BrowserContext=browser.new_context(storage_state=storage_state_path,record_video_dir="./videos")
        context.tracing.start(screenshots=True,snapshots=True,sources=True)
    yield context
    context.close()


@pytest.fixture
def login(
    homepage: HomePage,
    browser_context: BrowserContext,
    config: Config
):
    storage_state_path = Path("state") / config.environment / "state.json"

    if not storage_state_path.exists():
        homepage.login()
        browser_context.storage_state(path=storage_state_path)

    yield homepage

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
def page(config:Config,browser_context:BrowserContext):
    page:Page=browser_context.new_page()
    page.set_default_timeout(config.get_default_timeout())
    page.set_default_navigation_timeout(config.get_navigation_timeout())
    page.goto(config.get_base_url())
    yield page
    page.close()


@pytest.fixture
def homepage(page):
    homepage=HomePage(page)
    return homepage





@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    outcome = yield
    report: TestReport = outcome.get_result()
    if report.when == "call":
        evidence_manager = EvidenceManager(item, report)
        evidence_manager.handle_evidences_for_tc()
        evidence_manager.print_failed_test_case_report()