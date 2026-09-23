



from playwright.async_api import Page

from src.pages.reports_page import ReportsPage


class EmployerHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.heading_selector = self.page.get_by_text("Total Reviews", exact=True)
        self.reports_button = self.page.locator("div[class='css-146c3p1 font-pn-600 leading-5 select-none max-w-[90%] md:max-w-auto text-primary-text tracking-[0.25px] !text-grey-600']").nth(15)


    def click_reports_button(self)->ReportsPage:
        self.reports_button.click()
        return ReportsPage(self.page)

