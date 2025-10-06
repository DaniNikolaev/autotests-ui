import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return "Link"

    def check_have_attribute(self, name: str, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        with allure.step(f'Checking that {self.type_of} "{self.name}" has attribute "{value}"'):
            expect(locator).to_have_attribute(name, value)
