from playwright.sync_api import Page
import re
from pages.employer_login_page import EmployerLoginPage
from src.utils.logger import get_logger

class HomePage:

    def __init__(self,page:Page):
        self.page=page

        self.login_button=self.page.get_by_role("button",name=re.compile("Login"))
        self.title="Employer Dashboard | AmbitionBox"
        self.logger = get_logger(__name__.split(".")[-1])

    def go_to_employer_login_page(self)->EmployerLoginPage:
        self.logger.info("Going to click Login")
        self.login_button.click()
        self.logger.debug("Clicked Login Element")
        return EmployerLoginPage(self.page)
        
    def get_page_title(self)->str:
        return self.title

