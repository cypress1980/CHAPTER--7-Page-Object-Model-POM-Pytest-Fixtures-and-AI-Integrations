import re
from playwright.sync_api import Page, expect
def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("img", name="company-branding")).to_be_visible()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button",name ="Upgrade")).to_be_visible()
    page.get_by_role("link", name="Dashboard").click()
    expect(page.get_by_role("navigation", name="Sidepanel")).to_be_visible()
    page.get_by_role("link", name="Performance").click()
    expect(page.get_by_role("navigation", name="Sidepanel")).to_be_visible()
    page.get_by_role("link", name="Recruitment").click()
    expect(page.get_by_role("navigation", name="Sidepanel")).to_be_visible()