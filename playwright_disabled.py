from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('')

    login_button = page.get_by_test_id('login-page-login- button')
    expect(login_button).to_be_disabled()

    page.wait_for_timeout(5000)
