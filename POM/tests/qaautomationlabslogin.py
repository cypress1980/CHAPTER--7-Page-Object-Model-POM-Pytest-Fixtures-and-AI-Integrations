import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect,Page
from pages.qaautomationlabs_login_page import LoginPage
from pages.qaautomationlabs_home_page import HomePage

def test_Login():
    load_dotenv()  # loads .env file into environment
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        home_page = HomePage(page)
        login_page.goto()
        login_page.enterUsername(username)
        login_page.enterPassword(password)
        login_page.clickLogin()
        home_page.verifyLoginSuccess()
        home_page.clickDashboard()
        home_page.clickPerformance()
        home_page.clickRecruitment()
        browser.close()