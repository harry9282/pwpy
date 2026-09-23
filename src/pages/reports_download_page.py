from pathlib import Path
from playwright.sync_api import Page


class ReportsDownloadPage:
    def __init__(self, page: Page):
        self.page = page


    def download_report(self, path: Path):
        with self.page.expect_download() as download_info:  
            pass
        download_file_name:str = download_info.value.suggested_filename
        download_info.value.save_as(path/download_file_name)
        