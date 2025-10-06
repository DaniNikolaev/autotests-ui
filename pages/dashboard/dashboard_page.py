from playwright.sync_api import Page

from components.sidebar.sidebar_component import SidebarComponent
from components.charts.chart_view_component import ChartComponent
from components.navbar.navbar_component import NavbarComponent
from components.toolbars.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)
        self.students_chart = ChartComponent(page, "students", "bar")
        self.activities_chart = ChartComponent(page, "activities", "line")
        self.courses_chart = ChartComponent(page, "courses", "pie")
        self.scores_chart = ChartComponent(page, "scores", "scatter")
