import pytest
import allure
from allure_commons.types import Severity

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
@pytest.mark.regression
@pytest.mark.register
class TestRegister:
    @allure.title("Successful registration with correct credits")
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.xdist_group(name="authorization")
    @pytest.mark.parametrize('email, username, password',
                             [
                                 ('user.name1@gmail.com', 'username1', 'password1'),
                                 ('user.name2@gmail.com', 'username2', 'password2'),
                                 ('user.name3@gmail.com', 'username3', 'password3'),
                             ])
    def test_successful_registration_with_params(self,
                                                 registration_page: RegistrationPage,
                                                 dashboard_page: DashboardPage,
                                                 email: str,
                                                 username: str,
                                                 password: str):
        registration_page.registration_form.fill(email, username, password)
        registration_page.click_registration()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_navbar_visible(username)
        dashboard_page.sidebar.check_visible()

    @allure.title("Successful login after logout after registration")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize('email, username, password',
                             [
                                 ('user.name1@gmail.com', 'username1', 'password1'),
                                 ('user.name2@gmail.com', 'username2', 'password2'),
                                 ('user.name3@gmail.com', 'username3', 'password3'),
                             ])
    def test_successful_login_after_registration(self,
                                                 login_page: LoginPage,
                                                 registration_page: RegistrationPage,
                                                 dashboard_page: DashboardPage,
                                                 email: str,
                                                 username: str,
                                                 password: str):
        registration_page.registration_form.fill(email, username, password)
        registration_page.click_registration()

        dashboard_page.check_current_url(
            AppRoute.DASHBOARD)
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_navbar_visible(username)
        dashboard_page.sidebar.check_visible()

        dashboard_page.sidebar.click_logout()

        login_page.login_form.check_visible()
        login_page.check_login_visible()
        login_page.check_registration_visible()

        login_page.login_form.fill(email=email, password=password)
        login_page.click_login()

        dashboard_page.check_current_url(
            AppRoute.DASHBOARD)
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_navbar_visible(username)
        dashboard_page.sidebar.check_visible()

    @allure.title("Test visibility registration form")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("email, username, password",
                             [
                                 ("user@user.com", "user", "pass"),
                                 ("user1@user.com", "user1", "pass1"),
                                 ("user2@user.com", "user2", "pass2")
                             ])
    def test_registration_form(self,
                               registration_page: RegistrationPage,
                               email: str,
                               username: str,
                               password: str
                               ):
        registration_page.visit(
            AppRoute.REGISTRATION)
        registration_page.registration_form.fill(email, username, password)
        registration_page.registration_form.check_visible(email, username, password)

    @allure.title("Test URL after click login and check visibility")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_registration_to_login(self,
                                                 login_page: LoginPage,
                                                 registration_page: RegistrationPage
                                                 ):
        registration_page.click_login()
        login_page.check_current_url(
            AppRoute.LOGIN)
        login_page.login_form.check_visible()
