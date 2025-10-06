import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = Button(page, 'login-page-login-button', "Login")
        self.registration_link = Link(page, 'login-page-registration-link', "Registration")
        self.login_page_wrong_email_or_password_alert = Text(page,
                                                             'login-page-wrong-email-or-password-alert',
                                                             "Wrong email or password")

    @allure.step("Checking visible wrong email or password alert")
    def check_wrong_email_or_password_alert(self):
        self.login_page_wrong_email_or_password_alert.check_visible()
        self.login_page_wrong_email_or_password_alert.check_have_text('Wrong email or password')

    def check_login_visible(self):
        self.login_button.check_visible()

    def click_login(self):
        self.login_button.click()

    def check_registration_visible(self):
        self.login_button.check_visible()

    def click_registration(self):
        self.registration_link.click()
