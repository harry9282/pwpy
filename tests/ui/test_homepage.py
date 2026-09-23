from playwright.sync_api import expect
from src.pages.home_page import HomePage
from src.pages.employer_login_page import EmployerLoginPage
from src.pages.employer_home_page import EmployerHomePage
from src.pages.otp_page import OtpPage
from src.pages.reports_page import ReportsPage
from src.pages.reports_download_page import ReportsDownloadPage
from time import sleep
from pathlib import Path
from src.utils.assertions import verify
import pytest

from utils.data_manager import get_data


@pytest.mark.sanity
@pytest.mark.parametrize("user_data",get_data("emp_login.json"))
def test_employer_sanity_login(homepage,user_data):
    email, otp = user_data
    employer_login_page: EmployerLoginPage = homepage.go_to_employer_login_page()
    expect(employer_login_page.heading_selector).to_be_visible()
    otp_page: OtpPage = employer_login_page.enter_email_and_submit(email)
    verify("OTP page heading is visible", lambda: expect(otp_page.otp_page_heading).to_be_visible())
    sleep(2)
    employer_home_page: EmployerHomePage = otp_page.enter_otp(otp)
    verify("OTP page heading is not visible", lambda: expect(otp_page.otp_page_heading).not_to_be_visible())
    verify("Employer home page heading is visible", lambda: expect(employer_home_page.heading_selector).to_be_visible())
    reports_page: ReportsPage = employer_home_page.click_reports_button()
    verify("GENAI report button is visible", lambda: expect(reports_page.genai_report_button).to_be_visible())
    reports_download_page: ReportsDownloadPage = reports_page.click_genai_report_button()
    reports_download_page.download_report(Path("./downloads"))    



@pytest.mark.regression
@pytest.mark.parametrize("user_data",get_data("emp_login.json"))
def test_employer_regression_login(homepage,user_data):
    email, otp = user_data
    employer_login_page: EmployerLoginPage = homepage.go_to_employer_login_page()
    expect(employer_login_page.heading_selector).to_be_visible()
    otp_page: OtpPage = employer_login_page.enter_email_and_submit(email)
    verify("OTP page heading is visible", lambda: expect(otp_page.otp_page_heading).to_be_visible())
    sleep(2)
    employer_home_page: EmployerHomePage = otp_page.enter_otp(otp)
    verify("OTP page heading is not visible", lambda: expect(otp_page.otp_page_heading).not_to_be_visible())
    verify("Employer home page heading is visible", lambda: expect(employer_home_page.heading_selector).to_be_visible())
    reports_page: ReportsPage = employer_home_page.click_reports_button()
    verify("GENAI report button is visible", lambda: expect(reports_page.genai_report_button).to_be_visible())
    reports_download_page: ReportsDownloadPage = reports_page.click_genai_report_button()
    reports_download_page.download_report(Path("./downloads"))    



