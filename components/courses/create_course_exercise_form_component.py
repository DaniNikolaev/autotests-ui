import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from elements.input import Input


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.subtitle = Text(page, "create-course-exercise-{index}-box-toolbar-subtitle-text", "Subtitle")
        self.button = Button(page, "create-course-exercise-{index}-box-toolbar-delete-exercise-button", "Button")
        self.title_input = Input(page, "create-course-exercise-form-title-{index}-input", "Title")
        self.description_input = Input(page, "create-course-exercise-form-description-{index}-input", "Description")

    @allure.step('Checking that subtitle at index "{index}" is visible and has text')
    def check_subtitle(self, index: int):
        self.subtitle.check_visible(index=index)
        self.subtitle.check_have_text(f"#{index + 1} Exercise", index=index)

    def check_delete_button(self, index: int):
        self.button.check_visible(index=index)

    def click_delete_button(self, index: int):
        self.button.click(index=index)

    @allure.step('Fill and check that exercise create form at index "{index}" has values')
    def check_form(self,
                   index: int,
                   title: str = "Exercise title",
                   description: str = "Exercise description"):
        self.title_input.check_visible(index=index)
        self.title_input.fill(title, index=index)
        self.title_input.check_have_value(title, index=index)

        self.description_input.check_visible(index=index)
        self.description_input.fill(description, index=index)
        self.description_input.check_have_value(description, index=index)
