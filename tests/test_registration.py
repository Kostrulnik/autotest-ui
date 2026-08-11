from playwright.sync_api import sync_playwright, Page, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successufl_registration(chromium_page, initialize_browser_state: Page):
    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
