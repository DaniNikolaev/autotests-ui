import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', "Title")
        self.estimated_time_input = Input(page,
                                          'create-course-form-estimated-time-input', "Estimated time")
        self.description_textarea = Textarea(page,
                                             'create-course-form-description-input', "Description")
        self.max_score_input = Input(page, 'create-course-form-max-score-input', "Max score")
        self.min_score_input = Input(page, 'create-course-form-min-score-input', "Min score")

    @allure.step("Checking that create course form is visible")
    def check_visible(self,
                      title: str = "",
                      estimated_time: str = "",
                      description: str = "",
                      max_score: str = "0",
                      min_score: str = "0"
                      ):
        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_value(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(min_score)

    @allure.step("Fill create course forme")
    def fill(self,
             title: str,
             estimated_time: str,
             description: str,
             max_score: str = "0",
             min_score: str = "0"
             ):
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    @allure.step("Clear create course form")
    def clear(self):
        self.title_input.clear()
        self.estimated_time_input.clear()
        self.description_textarea.clear()
        self.max_score_input.clear()
        self.min_score_input.clear()
