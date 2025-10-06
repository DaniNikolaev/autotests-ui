import pytest
import allure


from pages.courses.course_create_page import CourseCreatePage
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.CREATE_COURSE)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.CREATE_COURSE)
@pytest.mark.create_course
@pytest.mark.regression
class TestCreateCourse:
    @allure.title("Test visibility create course toolbar")
    def test_toolbar(self, course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.toolbar.check_visible()

    @allure.title("Test empty view before upload image")
    def test_image_empty_view(self, course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.image_upload_widget.check_image_form_empty_view_()

    @allure.title("Test fully view after upload image")
    def test_image_fully_view(self, course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.image_upload_widget.upload_image()
        course_create_page_with_state.image_upload_widget.check_image_form_fully_view()

    @allure.title("Test image form upload image")
    def test_image_upload_empty_view(self, course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.image_upload_widget.check_upload_image_form()

    @allure.title("Test image form after upload image")
    def test_image_upload_fully_view(self, course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.image_upload_widget.upload_image()
        course_create_page_with_state.image_upload_widget.check_upload_image_form(is_uploaded=True)

    @allure.title("Test fill and visibility create course form")
    @pytest.mark.parametrize('title, estimated_time, description, max_score, min_score',
                             [
                                 ('Course #1', '1h 25m', "course #1", "12", "1"),
                                 ('Course #2', '2h 25m', "course #2", "11", "3"),
                                 ('Course #3', '3h 25m', "course #3", "9", "5"),
                                 ('', '', "", "0", "0"),
                                 ('Course #5', '5h 25m', "course #5", "100", "1"),
                             ])
    def test_course_create_form(self,
                                course_create_page_with_state: CourseCreatePage,
                                title: str,
                                estimated_time: str,
                                description: str,
                                max_score: str,
                                min_score: str
                                ):
        course_create_page_with_state.course_form.fill(title, estimated_time, description, max_score, min_score)
        course_create_page_with_state.course_form.check_visible(title, estimated_time, description, max_score,
                                                                min_score)

    @allure.title("Test visibility create exercises toolbar")
    def test_exercises_toolbar(self, course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.exercises_toolbar.check_visible()

    @allure.title("Test empty view before create exercises")
    def test_exercises_empty_view(self, course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.check_exercises_empty_view()

    @pytest.mark.parametrize('index', [0])
    def test_exercise_subtitle(self, course_create_page_with_state: CourseCreatePage, index: int):
        course_create_page_with_state.exercises_toolbar.click_create_exercise_button()
        course_create_page_with_state.create_exercise_form.check_subtitle(index)

    @pytest.mark.parametrize('index', [0])
    def test_exercise_delete_button(self, course_create_page_with_state: CourseCreatePage, index: int):
        course_create_page_with_state.exercises_toolbar.click_create_exercise_button()
        course_create_page_with_state.create_exercise_form.check_delete_button(index)

    @pytest.mark.parametrize('index, title, description',
                             [
                                 (0, "Ex #1", "Desc #1"),
                                 (0, "Ex #2", "Desc #2"),
                                 (0, "", ""),
                                 (0, "Ex #4", "Desc #4")
                             ]
                             )
    def test_exercise_create_form(self,
                                  course_create_page_with_state: CourseCreatePage,
                                  index: int,
                                  title: str,
                                  description: str):
        course_create_page_with_state.exercises_toolbar.click_create_exercise_button()
        course_create_page_with_state.create_exercise_form.check_form(index, title, description)
