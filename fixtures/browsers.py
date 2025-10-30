import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config import settings
from pages.authentication.registration_page import RegistrationPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.course_create_page import CourseCreatePage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute


@pytest.fixture(params=settings.browsers)
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(AppRoute.REGISTRATION)

    registration_page.registration_form.fill(email=settings.test_user.email,
                                             username=settings.test_user.username,
                                             password=settings.test_user.password)
    registration_page.click_registration()

    context.storage_state(path=settings.browser_state_file)


@pytest.fixture(params=settings.browsers)
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright,
                                          test_name=request.node.name,
                                          storage_state=settings.browser_state_file,
                                          browser_type=request.param)


@pytest.fixture(scope='session')
def initialize_browser_state_with_courses(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(AppRoute.REGISTRATION)

    registration_page.registration_form.fill(email=settings.test_user.email,
                                             username=settings.test_user.username,
                                             password=settings.test_user.password)
    registration_page.click_registration()

    courses_page = CoursesListPage(page)
    courses_page.visit(AppRoute.COURSES)
    courses_page.toolbar.click_create_course()

    course_create_page = CourseCreatePage(page)
    course_create_page.image_upload_widget.upload_image()

    course_create_page.course_form.fill(title="Test course #1",
                                        estimated_time="1h 20m",
                                        description="Test #1",
                                        max_score='10',
                                        min_score='1')
    course_create_page.toolbar.click_create_button()

    courses_page.toolbar.click_create_course()

    course_create_page.image_upload_widget.upload_image()
    course_create_page.course_form.fill(title="Test course #2",
                                        estimated_time="2h 30m",
                                        description="Test #2",
                                        max_score='12',
                                        min_score='3')
    course_create_page.toolbar.click_create_button()
    context.storage_state(path='browse-state_with_courses.json')


@pytest.fixture(params=settings.browsers)
def chromium_page_with_state_with_courses(initialize_browser_state_with_courses,
                                          request: SubRequest,
                                          playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright,
                                          test_name=request.node.name,
                                          storage_state='browse-state_with_courses.json',
                                          browser_type=request.param)
