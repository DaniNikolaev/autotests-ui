from playwright.sync_api import Page

from pages.base_page import BasePage
from components.empty_view.empty_view_component import EmptyViewComponent
from components.courses.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.toolbars.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.toolbars.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent


class CourseCreatePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar = CreateCourseToolbarViewComponent(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, "create-course-preview")

        self.course_form = CreateCourseFormComponent(page)

        self.exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)

        self.course_exercises_empty_view = EmptyViewComponent(page, "create-course-exercises")
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

    def check_exercises_empty_view(self):
        self.course_exercises_empty_view.check_visible(
            title="There is no exercises",
            description='Click on "Create exercise" button to create new exercise'
        )
