from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', "Registration")
        self.login_link = Link(page, 'registration-page-login-link', "Login")

    def check_visible_registration(self):
        self.registration_button.check_visible()
        self.registration_button.check_enabled()

    def check_visible_login(self):
        self.login_link.check_visible()
        self.login_link.check_have_attribute("href", "#/auth/login")

    def click_login(self):
        self.login_link.click()

    def click_registration(self):
        self.registration_button.click()
