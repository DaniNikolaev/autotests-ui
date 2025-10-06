import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, url: str):
        step = f'Checking that page URL is "{self.page.url}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(url)
