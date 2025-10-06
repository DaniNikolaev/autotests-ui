from playwright.sync_api import sync_playwright, expect


def check_alert_with_incorrect_credits():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        page.wait_for_timeout(1500)
        email_input=page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        page.wait_for_timeout(1500)
        password_input=page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill("password")

        page.wait_for_timeout(1500)
        login_button=page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_alert=page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

        page.wait_for_timeout(5000)

def check_elements_on_reg_and_auth_pages():
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input')

        password_input = page.get_by_test_id('login-form-password-input')

        login_button = page.get_by_test_id('login-page-login-button')

        expect(email_input).to_be_visible()
        expect(password_input).to_be_visible()
        expect(login_button).to_be_visible()

        registration_button=page.get_by_test_id('login-page-authentication-link')
        page.wait_for_timeout(1500)
        registration_button.click()
        page.wait_for_timeout(1500)

        email_input_reg = page.get_by_test_id('authentication-form-email-input')

        password_input_reg = page.get_by_test_id('authentication-form-password-input')

        reg_button = page.get_by_test_id('authentication-page-authentication-button')

        expect(email_input_reg).to_be_visible()
        expect(password_input_reg).to_be_visible()
        expect(reg_button).to_be_visible()
        page.wait_for_timeout(3000)
