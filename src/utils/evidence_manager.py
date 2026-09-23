

from playwright.sync_api import Page,BrowserContext,Browser
import os
from pathlib import Path
from pytest import Item
from pytest import TestReport
import allure




class EvidenceManager:
    def __init__(self,item:Item,report:TestReport):
      
        self.item=item
        self.report=report


    def handle_evidences_for_tc(self):
        if self.report.failed:
            browser_context:BrowserContext = self.item.funcargs.get("browser_context")
            if not browser_context:
                print("Browser Context Not Found")
                return
            pages:list[Page]=browser_context.pages
            size=len(pages)
            if size==1:
                print("No Action need")
            elif size>1:
                for page in pages[:-1]:
                    video_path = page.video.path()
                    if video_path:
                        os.remove(video_path)
            page:Page=pages[-1]
            if page:
                page.screenshot(path=f"./screenshots/{self.item.name}_failed.png")
                allure.attach.file(f"./screenshots/{self.item.name}_failed.png", name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
                
                browser_context.tracing.stop(path=f"./traces/{self.item.name}_failed.zip")
                allure.attach.file(f"./traces/{self.item.name}_failed.zip", name="Execution Trace", attachment_type=allure.attachment_type.ZIP)
                
                video_path:Path = page.video.path()
                if video_path:
                    allure.attach.file(video_path, name="Execution Video", attachment_type=allure.attachment_type.WEBM)
        if self.report.passed:
            browser_context:BrowserContext = self.item.funcargs.get("browser_context")
            if not browser_context:
                print("Browser Context Not Found")
                return
            browser_context.tracing.stop()
            pages:list[Page]=browser_context.pages
            for page in pages:
                if page:
                    video_path:Path = page.video.path()
                    if video_path:
                        os.remove(video_path)
            page=pages[-1]
            if page:
                with allure.step(f"Test Case Passed: {self.item.name}"):
                    page.screenshot(path=f"./screenshots/{self.item.name}_passed.png")
                    allure.attach.file(f"./screenshots/{self.item.name}_passed.png",name=f"{self.item.name}_passed",attachment_type=allure.attachment_type.PNG)

    def print_failed_test_case_report(self):
        if self.report.failed:
            file_and_line = str(self.report.longrepr.reprcrash.path) + ":" + str(self.report.longrepr.reprcrash.lineno)
            error_message  = str(self.report.longrepr.reprcrash.message)
            
            # Use allure.attach to cleanly add error details to the report
            failure_details = f"Location: {file_and_line}\n\nError Message:\n{error_message}"
            allure.attach(failure_details, name="Failure Details", attachment_type=allure.attachment_type.TEXT)
            
            # Print cleanly to terminal
            print(f"\n❌ Test Case Failed: {self.item.name}")
            print(f"📍 Location of Failure: {file_and_line}")
            print(f"💥 Error Message: {error_message}\n")