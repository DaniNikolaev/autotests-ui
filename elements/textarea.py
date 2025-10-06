import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("TEXTAREA")


class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return "Textarea"

    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth=nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        step = f'Fill {self.type_of} "{self.name}" at index "{nth}" to value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator.fill(value)

    def clear(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        step = f'Clear {self.type_of} "{self.name}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            locator.clear()

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" has value "{value}"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_value(value)
