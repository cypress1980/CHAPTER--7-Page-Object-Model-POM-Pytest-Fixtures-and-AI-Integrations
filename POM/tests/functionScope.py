# test_function_scope.py
import pytest

@pytest.fixture(scope="function")
def user():
    print("\n[SETUP] Creating a fresh product")
    yield {"id": 1, "name": "Mango"}
    print("[TEARDOWN] Deleting product")

def test_user_name(user):
    assert user["name"] == "Mango"

def test_user_id(user):
    assert user["id"] == 1