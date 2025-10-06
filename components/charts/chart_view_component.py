import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.image import Image


class ChartComponent(BaseComponent):
    def __init__(self, page: Page, name: str, chart_type: str):
        super().__init__(page)

        self.name = name.capitalize()
        self.title = Text(page, f'{name}-widget-title-text', "Title")
        self.chart = Image(page, f'{name}-{chart_type}-chart', "Chart")

    def check_chart_and_title(self):
        with allure.step(f'Check that title and chart is visible and title has text "{self.name}"'):
            self.title.check_visible()
            self.title.check_have_text(self.name)
            self.chart.check_visible()
