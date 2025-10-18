import os
from playwright.sync_api import sync_playwright, expect

def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        
        # Ensure test-results directory exists
        os.makedirs("test-results", exist_ok=True)
        
        # Start tracing
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        try:
            page = context.new_page()
            page.goto("https://shop.qaautomationlabs.com/index.php")
            
            # Fill email and password
            page.fill('input[id="email"]', 'demo@demo.com')
            page.fill('input[id="password"]', 'demo')
            
            # Locate the login button
            login_button = page.locator('button[id="loginBtn"]')
            
            # Assert button is visible and enabled
            expect(login_button).to_be_visible()
            expect(login_button).to_be_enabled()
            
            # Click the login button
            login_button.click()
            page.wait_for_timeout(2000)
            
            # Verify successful login
            expect(page.locator("#navbarCollapse")).to_contain_text("Home")
            
        finally:
            # This will always execute, even if test fails
            context.tracing.stop(path="test-results/trace.zip")
            context.close()
            browser.close()