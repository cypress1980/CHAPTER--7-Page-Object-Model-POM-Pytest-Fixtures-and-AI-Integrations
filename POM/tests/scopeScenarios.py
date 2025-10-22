import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, expect

# Session scoped - fixture: Launch browser once for the entire test session
@pytest.fixture(scope="session")
def browser():
    print("=== SESSION: Launching browser ===")
    with sync_playwright() as p:
        browser_instance = p.chromium.launch(headless=False)  # Visible for demo
        yield browser_instance
        print("=== SESSION: Closing browser ===")
        browser_instance.close()

# Module scoped - fixture: Create a browser context once per module (file)
@pytest.fixture(scope="module")
def context(browser):
    print("=== MODULE: Creating browser context ===")
    context_instance = browser.new_context()
    yield context_instance
    print("=== MODULE: Closing browser context ===")
    context_instance.close()

# Function-scoped - fixture: Runs per test function (e.g., for isolated actions)
@pytest.fixture(scope="function")
def take_screenshot(context):
    def _screenshot(page, name="screenshot"):
        print(f"=== FUNCTION: Taking screenshot for {name} ===")
        page.screenshot(path=f"{name}.png")
    yield _screenshot

# Standalone function tests (no class) to demo function/module/session scopes
def test_home_page_title(context, take_screenshot):
    page = context.new_page()
    page.goto("https://naveenautomationlabs.com/opencart/")
    assert "Your Store" in page.title()  # Fixed: Actual title is "Your Store"
    take_screenshot(page, "home_page")
    page.close()

def test_search_functionality(context, take_screenshot):
    page = context.new_page()
    page.goto("https://naveenautomationlabs.com/opencart/")
    page.fill('input[name="search"]', "iPhone")
    page.click('.input-group-btn')
    assert page.locator('h1').inner_text() == "Search - iPhone"
    take_screenshot(page, "search_results")
    page.close()

# Class-based tests to demo class scope alongside others
# class TestProductPage:
#     Class-scoped fixture: Runs once per class (setup for all methods)
@pytest.fixture(scope="class")
def setup_page(context):
    print("=== CLASS: Navigating to products page ===")
    page = context.new_page()
    page.goto("https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=20")
    yield page
    print("=== CLASS: Closing class page ===")
    page.close()

def test_product_count(setup_page, take_screenshot):
    setup_page.wait_for_selector("h4 a", state="visible", timeout=15000)
    count = setup_page.locator("h4 a").count()
    assert count > 0
    take_screenshot(setup_page, "product_count")

def test_first_product_link(setup_page, take_screenshot):
    first_link = setup_page.locator("h4 a").first
    first_link.click()
    assert "Apple Cinema 30" in setup_page.title()
    take_screenshot(setup_page, "first_product")