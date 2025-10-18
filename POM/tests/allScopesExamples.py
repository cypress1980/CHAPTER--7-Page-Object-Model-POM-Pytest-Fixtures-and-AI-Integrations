import pytest
from playwright.sync_api import sync_playwright, expect

# ============================================================================
# BROWSER & CONTEXT FIXTURES (Shared Resources)
# ============================================================================

@pytest.fixture(scope="session")
def browser():
    """Single browser instance for entire test session"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """New context for each test - ensures isolation"""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """New page for each test"""
    page = context.new_page()
    yield page


# ============================================================================
# NAVIGATION FIXTURES
# ============================================================================

@pytest.fixture(scope="function")
def home_page(page):
    """Navigate to home page"""
    page.goto("https://shop.qaautomationlabs.com/index.php")
    yield page


# ============================================================================
# AUTHENTICATION FIXTURES
# ============================================================================

@pytest.fixture(scope="function")
def logged_in_page(home_page):
    home_page.fill('[id="email"]', 'demo@demo.com')
    home_page.fill('[id="password"]', 'demo')
    home_page.click('[id="loginBtn"]')
    yield home_page


# ============================================================================
# TESTS
# ============================================================================

def test_basic_navigation(page):
    """Test basic page navigation without login"""
    page.goto("https://shop.qaautomationlabs.com/index.php")
    expect(page).to_have_url("https://shop.qaautomationlabs.com/index.php")


def test_login_functionality(home_page):
    """Test login process"""
    home_page.fill('[id="email"]', 'demo@demo.com')
    home_page.fill('[id="password"]', 'demo')
    home_page.click('[id="loginBtn"]')
    expect(home_page).to_have_url("https://shop.qaautomationlabs.com/shop.php")


def test_with_logged_in_user(logged_in_page):
    """Test that requires authenticated user"""
    expect(logged_in_page).to_have_url("https://shop.qaautomationlabs.com/shop.php")
    # Add your test logic here


class TestUserDashboard:
    """Group related tests in a class"""
    
    def test_dashboard_access(self, logged_in_page):
        """Test dashboard is accessible"""
        expect(logged_in_page).to_have_url("https://shop.qaautomationlabs.com/shop.php")
    
    def test_user_profile(self, logged_in_page):
        """Test user profile features"""
        # Each test gets its own login session
        expect(logged_in_page).to_have_url("https://shop.qaautomationlabs.com/shop.php")


# ============================================================================
# ADVANCED: State Reuse Pattern (for performance-critical scenarios)
# ============================================================================

@pytest.fixture(scope="session")
def authenticated_state(browser):
    """
    Create reusable authentication state - use sparingly!
    Only for tests that don't modify user state.
    """
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://shop.qaautomationlabs.com/index.php")
    page.fill('[id="email"]', 'demo@demo.com')
    page.fill('[id="password"]', 'demo')
    page.click('[id="loginBtn"]')

    # Save authenticated state
    storage = context.storage_state()
    context.close()
    return storage


@pytest.fixture(scope="function")
def fast_logged_in_page(browser, authenticated_state):
    """
    Fast login using saved state - for read-only tests.
    WARNING: Don't use if tests modify user data!
    """
    context = browser.new_context(storage_state=authenticated_state)
    page = context.new_page()
    page.goto("https://shop.qaautomationlabs.com/index.php")
    yield page
    context.close()


def test_fast_authenticated_access(fast_logged_in_page):
    """Example of fast authenticated test"""
    expect(fast_logged_in_page).to_have_url("https://shop.qaautomationlabs.com/index.php")