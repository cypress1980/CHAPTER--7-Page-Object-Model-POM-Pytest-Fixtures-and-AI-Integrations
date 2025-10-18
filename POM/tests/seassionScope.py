# conftest.py (or in any test file)
import pytest

@pytest.fixture(scope="session")
def global_config():
    print("\n[SETUP] Loading global config (once per session)")
    config = {"env": "test", "timeout": 30}
    yield config
    print("[TEARDOWN] Cleaning up global config")

# test_session_scope.py
def test_env(global_config):
    assert global_config["env"] == "test"

def test_timeout(global_config):
    assert global_config["timeout"] == 30