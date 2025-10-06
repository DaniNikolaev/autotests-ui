import pytest
import allure
from allure_commons.types import Severity


from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
@pytest.mark.regression
@pytest.mark.authorization
class TestAuth:
    @allure.title("Test alert after login with incorrect credits")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.xdist_group(name="authorization")
    @pytest.mark.parametrize('email, password',
                             [("user.name@gmail.com", "password"),
                              ("user.name@gmail.com", "  "),
                              ("  ", "password")
                              ])
    def test_alert_with_incorrect_credits(self, login_page: LoginPage, email: str, password: str):
        login_page.login_form.fill(email, password)
        login_page.click_login()
        login_page.check_wrong_email_or_password_alert()

    @allure.title("Test visibility login form")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize('email, password',
                             [("user.name@gmail.com", "password"),
                              ("user.name@gmail.com", "  "),
                              ("  ", "password")
                              ])
    def test_login_form(self, login_page: LoginPage, email: str, password: str):
        login_page.login_form.fill(email, password)
        login_page.login_form.check_visible(email, password)

    @allure.title("Test URL after click registration and check visibility")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_login_to_registration(self,
                                                 registration_page: RegistrationPage,
                                                 login_page: LoginPage,
                                                 ):
        login_page.click_registration()
        registration_page.check_current_url(
            AppRoute.REGISTRATION)
        registration_page.registration_form.check_visible()
