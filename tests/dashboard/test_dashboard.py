import pytest
import allure

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    @allure.title("Check dashboard displaying navbar, sidebar and charts")
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.navbar.check_navbar_visible(settings.test_user.username)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.students_chart.check_chart_and_title()
        dashboard_page_with_state.activities_chart.check_chart_and_title()
        dashboard_page_with_state.courses_chart.check_chart_and_title()
        dashboard_page_with_state.scores_chart.check_chart_and_title()

    @allure.title("Check URL after click dashboard button")
    def test_dashboard_button(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.sidebar.click_dashboard()

    @allure.title("Check URL after click courses button")
    def test_courses_button(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.sidebar.click_courses()

    @allure.title("Check URL after click logout button")
    def test_logout_button(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.sidebar.click_logout()
