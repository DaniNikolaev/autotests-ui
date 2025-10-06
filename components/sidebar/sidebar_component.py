import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.sidebar.sidebar_list_item_component import SidebarListItemComponent
from tools.routes import AppRoute


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard")
        self.courses_list_item = SidebarListItemComponent(page, "courses")
        self.logout_list_item = SidebarListItemComponent(page, "logout")

    @allure.step("Checking that sidebar is visible")
    def check_visible(self):
        self.dashboard_list_item.check_visible()
        self.courses_list_item.check_visible()
        self.logout_list_item.check_visible()

    def click_dashboard(self):
        self.dashboard_list_item.navigate(
            AppRoute.DASHBOARD)

    def click_courses(self):
        self.courses_list_item.navigate(
            AppRoute.COURSES
        )

    def click_logout(self):
        self.logout_list_item.navigate(
            AppRoute.LOGIN
        )
