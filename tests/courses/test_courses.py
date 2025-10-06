import pytest
import allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.course_create_page import CourseCreatePage
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES_LIST)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES_LIST)
@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    @pytest.mark.courses_empty_view
    @pytest.mark.courses_full_view
    def test_empty_courses_list(self,
                                courses_page_with_state: CoursesListPage):
        courses_page_with_state.toolbar.check_visible()
        courses_page_with_state.navbar.check_navbar_visible("user")
        courses_page_with_state.sidebar.check_visible()
        courses_page_with_state.check_empty_view_form()

    @pytest.mark.courses_empty_view
    def test_courses_empty_view(self,
                                courses_page_with_state: CoursesListPage):
        courses_page_with_state.check_empty_view_form()

    @pytest.mark.courses_full_view
    @pytest.mark.parametrize('index', [0, 1])
    def test_courses_full_view_edit_button(self,
                                           courses_page_with_state_with_courses: CoursesListPage, index: int):
        courses_page_with_state_with_courses.course_card.menu.check_menu(index)

    @pytest.mark.courses_full_view
    @pytest.mark.parametrize('index', [0, 1])
    def test_courses_full_view_edit_course_item(self,
                                                courses_page_with_state_with_courses: CoursesListPage, index: int):
        courses_page_with_state_with_courses.course_card.menu.check_edit(index)

    @pytest.mark.courses_full_view
    @pytest.mark.parametrize('index', [0, 1])
    def test_courses_full_view_delete_course_item(self,
                                                  courses_page_with_state_with_courses: CoursesListPage, index: int):
        courses_page_with_state_with_courses.course_card.menu.check_delete(index)

    @pytest.mark.courses_full_view
    @pytest.mark.parametrize('index, title, max_score, min_score, estimated_time',
                             [
                                 (0, "Test course #1", "10", "1", "1h 20m"),
                                 (1, "Test course #2", "12", "3", "2h 30m")
                             ])
    def test_courses_full_view_course_card(self,
                                           courses_page_with_state_with_courses: CoursesListPage,
                                           index: int,
                                           title: str,
                                           max_score: str,
                                           min_score: str,
                                           estimated_time: str
                                           ):
        courses_page_with_state_with_courses.course_card.check_visible(index, title, max_score, min_score,
                                                                       estimated_time)

    @pytest.mark.create_course
    def test_create_course(self,
                           courses_page_with_state: CoursesListPage,
                           course_create_page_with_state: CourseCreatePage):
        course_create_page_with_state.toolbar.check_visible()
        course_create_page_with_state.image_upload_widget.check_image_form_empty_view_()
        course_create_page_with_state.image_upload_widget.check_upload_image_form()
        course_create_page_with_state.course_form.check_visible()
        course_create_page_with_state.exercises_toolbar.check_visible()
        course_create_page_with_state.check_exercises_empty_view()

        course_create_page_with_state.image_upload_widget.upload_image()
        course_create_page_with_state.image_upload_widget.check_image_form_fully_view()
        course_create_page_with_state.image_upload_widget.check_upload_image_form(is_uploaded=True)
        course_create_page_with_state.course_form.fill(
            title="Playwright", estimated_time="2 weeks", description="Playwright", max_score="100", min_score="10")
        course_create_page_with_state.course_form.fill(
            title="Playwright", estimated_time="2 weeks", description="Playwright", max_score="100", min_score="10"
        )
        course_create_page_with_state.toolbar.click_create_button()

        courses_page_with_state.toolbar.check_visible()
        courses_page_with_state.course_card.check_visible(
            index=0, title="Playwright", estimated_time="2 weeks", max_score="100", min_score="10")

    @pytest.mark.create_course
    @pytest.mark.edit_course
    def test_edit_course(self,
                         courses_page_with_state: CoursesListPage,
                         course_create_page_with_state: CourseCreatePage
                         ):
        course_create_page_with_state.image_upload_widget.upload_image()
        course_create_page_with_state.image_upload_widget.check_image_form_fully_view()

        course_create_page_with_state.course_form.fill(title="Test #1",
                                                       estimated_time="3h 50m",
                                                       description="Test #1",
                                                       max_score="10",
                                                       min_score="1")

        course_create_page_with_state.toolbar.click_create_button()

        courses_page_with_state.course_card.check_visible(index=0,
                                                          title="Test #1",
                                                          estimated_time="3h 50m",
                                                          max_score="10",
                                                          min_score="1")

        courses_page_with_state.course_card.menu.click_edit()

        course_create_page_with_state.course_form.clear()

        course_create_page_with_state.course_form.fill(title="Test #111",
                                                       estimated_time="33h 50m",
                                                       description="Test #111",
                                                       max_score="110",
                                                       min_score="11")

        course_create_page_with_state.toolbar.click_create_button()

        courses_page_with_state.course_card.check_visible(index=0,
                                                          title="Test #111",
                                                          estimated_time="33h 50m",
                                                          max_score="110",
                                                          min_score="11")
