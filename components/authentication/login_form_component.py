import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', "Title")
        self.email_input = Input(page, 'login-form-email-input', "Email")
        self.password_input = Input(page, 'login-form-password-input', "Password")

    @allure.step("Checking that login form is visible")
    def check_visible(self, email: str = "", password: str = ""):
        self.title.check_visible()
        self.title.check_have_text("UI Course")

        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)

    @allure.step("Filling email and password to login form")
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
