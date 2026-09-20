from playwright.sync_api import Page
import re

class HomePage:

    def __init__(self,page:Page):
        self.page=page

        self.heading=self.page.get_by_role("heading",name=re.compile(" on a Real Site"))
        self.grab_deal=self.page.get_by_text("Grab the Deal")
        self.title="WebDriverUniversity – Free Test Automation Practice Site (AI, Playwright, Selenium, Cypress"


    def go_to_udemy_dealpage(self):
        self.grab_deal.click()

    def get_page_title(self):
        return self.title

    def get_heading_of_homepage(self):
        return self.heading.inner_text()
