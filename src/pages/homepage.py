from playwright.sync_api import Page
import re
from src.pages.udemy import UdemyPage
from src.utils.logger import get_logger

class HomePage:

    def __init__(self,page:Page):
        self.page=page

        self.heading=self.page.get_by_role("heading",name=re.compile(" on a Real Site"))
        self.grab_deal=self.page.get_by_text("Grab the Deal").nth(0)
        self.title="WebDriverUniversity – Free Test Automation Practice Site (AI, Playwright, Selenium, Cypress)"
        self.logger = get_logger(__name__.split(".")[-1])


    def go_to_udemy_dealpage(self)->UdemyPage:
        with self.page.context.expect_page() as new_tab:
            self.logger.info("Going to click GrabDeal Element")
            self.grab_deal.click()
            self.logger.debug("Clicked GrabDeal Element")
        udemy_page:Page=new_tab.value
        self.logger.debug("Waiting for Page to Load")
        udemy_page.wait_for_load_state("load")
        self.logger.debug("Page Loaded Successfuly")

        return UdemyPage(udemy_page)
        
  

    def get_page_title(self)->str:
        return self.title

    def get_heading_of_homepage(self)->str:
        return self.heading.inner_text()
