from playwright.sync_api import Page

class UdemyPage:


    def __init__(self,page:Page):
        self.page=page
        self.heading="Claude Code & AI: Playwright Test Automation for QA"

    def get_current_url(self)->str:
        return self.page.url