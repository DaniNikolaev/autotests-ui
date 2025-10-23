from ui_coverage_tool import ActionType, SelectorType

from elements.ui_coverage import tracker
from tools.logger import get_logger

import allure
from playwright.sync_api import Page, expect, Locator


logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return "base_element"

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        locator = self.locator.format(**kwargs)
        return f"//*[@data-testid='{locator}'][{nth+1}]"

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs):
        tracker.track_coverage(selector=self.get_raw_locator(nth, **kwargs),
                               action_type=action_type,
                               selector_type=SelectorType.XPATH)

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with data-testid="{locator}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Clicking {self.type_of} "{self.name}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            locator.click()

        self.track_coverage(action_type=ActionType.CLICK, nth=nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is visible"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_visible()

        self.track_coverage(action_type=ActionType.VISIBLE, nth=nth, **kwargs)

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" has text "{text}"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(action_type=ActionType.TEXT, nth=nth, **kwargs)
