import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.course_create_page import CourseCreatePage
from tools.routes import AppRoute


@pytest.fixture()
def login_page(chromium_page: Page) -> LoginPage:
    p = LoginPage(page=chromium_page)
    p.visit(AppRoute.LOGIN)
    return p


@pytest.fixture()
def registration_page(chromium_page: Page) -> RegistrationPage:
    p = RegistrationPage(page=chromium_page)
    p.visit(AppRoute.REGISTRATION)
    return p


@pytest.fixture()
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)


@pytest.fixture()
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    p = DashboardPage(page=chromium_page_with_state)
    p.visit(AppRoute.DASHBOARD)
    return p


@pytest.fixture()
def courses_page_with_state(chromium_page_with_state: Page) -> CoursesListPage:
    p = CoursesListPage(page=chromium_page_with_state)
    p.visit(AppRoute.COURSES)
    return p


@pytest.fixture()
def courses_page_with_state_with_courses(chromium_page_with_state_with_courses: Page) -> CoursesListPage:
    p = CoursesListPage(page=chromium_page_with_state_with_courses)
    p.visit(AppRoute.COURSES)
    return p


@pytest.fixture()
def course_create_page_with_state(chromium_page_with_state) -> CourseCreatePage:
    p = CourseCreatePage(page=chromium_page_with_state)
    p.visit(AppRoute.CREATE_COURSE)
    return p
