import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "Button"

    def check_disabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is disabled'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_disabled()

        self.track_coverage(action_type=ActionType.DISABLED, nth=nth, **kwargs)

    def check_enabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is enabled'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_enabled()

        self.track_coverage(action_type=ActionType.ENABLED, nth=nth, **kwargs)
