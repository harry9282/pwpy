from playwright.sync_api import Page
from time import sleep

from src.pages.employer_home_page import EmployerHomePage


class OtpPage:
    def __init__(self, page: Page):
        self.page = page



        self.otp_input = self.page.locator("input[class='css-11aywtz r-6taxm2 border rounded-sm absolute w-[200px] h-[44px] opacity-0 z-10 r-van48c']")
        self.otp_page_heading=self.page.get_by_text("OTP Verification")

    def enter_otp(self, otp: str)->EmployerHomePage:
        self.otp_input.fill(otp)
        return EmployerHomePage(self.page)

