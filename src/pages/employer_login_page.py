from playwright.sync_api import Page
from src.pages.otp_page import OtpPage

class EmployerLoginPage:


    def __init__(self,page:Page):
        self.page=page
        self.heading_selector=self.page.get_by_text("Login/Signup for free!",exact=True)
        self.submit_button=self.page.get_by_role("button",name="Submit")
        self.email_input=self.page.get_by_test_id("workEmail_input")



    def enter_email_and_submit(self,email:str)-> OtpPage:
        self.email_input.fill(email)
        self.submit_button.click()
        return OtpPage(self.page)


   

   