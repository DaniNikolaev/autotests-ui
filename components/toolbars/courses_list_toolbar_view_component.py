import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from tools.routes import AppRoute


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', "Title")
        self.create_button = Button(page, 'courses-list-toolbar-create-course-button', "Button")

    @allure.step("Checking that courses list toolbar is visible")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Courses")

        self.create_button.check_visible()

    def click_create_course(self):
        self.create_button.click()
        self.check_current_url(
            AppRoute.CREATE_COURSE)
