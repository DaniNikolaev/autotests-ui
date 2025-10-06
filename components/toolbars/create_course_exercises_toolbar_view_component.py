import allure
from playwright.sync_api import expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', "Title")
        self.create_exercise_button = Button(page,
                                             'create-course-exercises-box-toolbar-create-exercise-button',
                                             "Button")

    @allure.step('Checking that exercises toolbar is visible and title has text "Exercises"')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Exercises")

        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
