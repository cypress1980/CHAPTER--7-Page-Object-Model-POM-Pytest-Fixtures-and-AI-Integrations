# test_module_scope.py
import pytest

@pytest.fixture(scope="module")
def browser():
    print("\n[SETUP] Launching browser (once per file)")
    browser_instance = "Chromium"
    yield browser_instance
    print("[TEARDOWN] Closing browser")

def test_homepage(browser):
    assert browser == "Chromium"

def test_login_page(browser):
    assert browser == "Chromium"