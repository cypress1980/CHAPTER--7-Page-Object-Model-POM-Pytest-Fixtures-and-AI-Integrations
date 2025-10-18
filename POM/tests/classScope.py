# test_class_scope.py
import pytest

@pytest.fixture(scope="class")
def database():
    print("\n[SETUP] Connecting to DB (once per class)")
    yield "db_connection"
    print("[TEARDOWN] Closing DB connection")

class TestUserQueries:
    def test_fetch_user(self, database):
        assert database == "db_connection"

    def test_update_user(self, database):
        assert database == "db_connection"