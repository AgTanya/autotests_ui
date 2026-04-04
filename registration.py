from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email = page.locator('//input[@id=":r0:"]')
    email.fill("user.name@gmail.com")

    user_name = page.get_by_test_id("registration-form-username-input").locator("input")
    user_name.fill("username")

    password = page.locator('//div[@data-testid="registration-form-password-input"]/div/input')
    password.fill("password")

    registration = page.get_by_test_id("registration-page-registration-button")
    registration.click()

    dashboard = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text("Dashboard")
