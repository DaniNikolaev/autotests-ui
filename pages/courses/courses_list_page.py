from playwright.sync_api import Page

from components.sidebar.sidebar_component import SidebarComponent
from components.navbar.navbar_component import NavbarComponent
from components.empty_view.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.toolbars.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.toolbar = CoursesListToolbarViewComponent(page)

        self.courses_empty_view = EmptyViewComponent(page, "courses-list")

        self.course_card = CourseViewComponent(page)
        # self.course_widget_title_text = page.get_by_test_id('course-widget-title-text')
        # self.course_edit_course_button = page.get_by_test_id('course-view-menu-button')
        # self.course_view_menu_edit_item = page.get_by_test_id('course-view-edit-menu-item')
        # self.course_view_menu_delete_item = page.get_by_test_id('course-view-delete-menu-item')
        # self.course_preview_image = page.get_by_test_id('course-preview-image')
        # self.course_max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        # self.course_min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        # self.course_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

    def check_empty_view_form(self):
        self.courses_empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here"
        )
