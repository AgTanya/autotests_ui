from playwright.sync_api import sync_playwright, expect

 # with as это контекстный менеджер, когда выходим из контекста браузер автоматически закрывается
with sync_playwright() as playwright:
    # запуск браузера headless=False чтобы мы видели
    browser = playwright.chromium.launch(headless=False)

    # создаем страницу и переходим по ссылке
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # находим поле, для заполнения email и вставляем данные
    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill('test@mail.ru')

    password_input = page.get_by_test_id("login-form-password-input").locator("input") # = page.locator('//div[@data-testid="login-form-password-input"]/div/input')
    password_input.fill('Qwerty12345')

    # Если в теге есть атрибут data-testid, то playwright может уже искать по нему
    login_button = page.get_by_test_id("login-page-login-button")
    login_button.click()

    # проверяем, что отображается валидация неверного логина/пароля
    wrong_email_or_password = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    #  проверяем, что блок виден
    expect(wrong_email_or_password).to_be_visible()
    # Проверим, что этот блок содержит конкретный текст
    expect(wrong_email_or_password).to_have_text("Wrong email or password")

    # тут будет падать сс ошибкой, так как проверка на скрытие блока
    # expect(wrong_email_or_password).to_be_hidden()



    # ждем 5 сек чтобы мы глазами увидели
    page.wait_for_timeout(5000)


