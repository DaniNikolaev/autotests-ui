from playwright.sync_api import sync_playwright, expect


def check_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        page.wait_for_timeout(1500)
        email_input = page.get_by_test_id('authentication-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        page.wait_for_timeout(1500)
        username_input = page.get_by_test_id('authentication-form-username-input').locator('input')
        username_input.fill('username')

        page.wait_for_timeout(1500)
        password_input = page.get_by_test_id('authentication-form-password-input').locator('input')
        password_input.fill('password')

        page.wait_for_timeout(1500)
        registration_button=page.get_by_test_id('authentication-page-authentication-button')
        registration_button.click()

        h6_title=page.get_by_test_id('dashboard-toolbar-title-text')
        expect(h6_title).to_be_visible()
        expect(h6_title).to_have_text('Dashboard')
        page.wait_for_timeout(1500)


def registration_with_save_state():
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        page.wait_for_timeout(1500)
        email_input = page.get_by_test_id('authentication-form-email-input').locator('input')
        email_input.fill('test@test.com')

        page.wait_for_timeout(1500)
        username_input = page.get_by_test_id('authentication-form-username-input').locator('input')
        username_input.fill('user')

        page.wait_for_timeout(1500)
        password_input = page.get_by_test_id('authentication-form-password-input').locator('input')
        password_input.fill('pass')

        page.wait_for_timeout(1500)
        registration_button = page.get_by_test_id('authentication-page-authentication-button')
        registration_button.click()

        context.storage_state(path='browse-state.json')


def auth_with_browse_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browse-state.json')
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(title).to_be_visible()
        expect(title).to_have_text('Courses')

        courses_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list_title).to_be_visible()
        expect(courses_list_title).to_have_text('There is no results')

        page.wait_for_timeout(50000)


#registration_with_save_state()
auth_with_browse_state()