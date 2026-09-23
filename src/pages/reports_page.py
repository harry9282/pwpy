from playwright.sync_api import Page, expect
from time import sleep

from src.pages.reports_download_page import ReportsDownloadPage


class ReportsPage:
    def __init__(self, page:Page):
        self.page = page
        self.genai_report_button = self.page.get_by_test_id("ownload_pulse_report_button").nth(0)


    def click_genai_report_button(self)->ReportsDownloadPage:
        with self.page.expect_popup() as popup_info:
            self.genai_report_button.click()
        page:Page = popup_info.value
        return ReportsDownloadPage(page)