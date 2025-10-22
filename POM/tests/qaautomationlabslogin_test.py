import os
import json
from playwright.sync_api import sync_playwright, expect,Page
from pages.qaautomationlabs_login_page import LoginPage
from pages.qaautomationlabs_home_page import HomePage

def test_Login():
    with open("config.json") as f:
        config = json.load(f)
    username = config["username"]
    password = config["password"]
    url = config["url"]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        home_page = HomePage(page)
        login_page.goto(url)
        login_page.enterUsername(username)
        login_page.enterPassword(password)
        login_page.clickLogin()
        home_page.verifyLoginSuccess()
        home_page.clickDashboard()
        home_page.clickPerformance()
        home_page.clickRecruitment()
        browser.close()