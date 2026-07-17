import os
from unittest import mock

import peewee
import pytest

os.environ.setdefault("MYSQL_DATABASE", "test")
os.environ.setdefault("MYSQL_USER", "test")
os.environ.setdefault("MYSQL_PASSWORD", "test")
os.environ.setdefault("MYSQL_HOST", "localhost")
os.environ.setdefault("URL", "localhost:5000")

# app/__init__.py connects to MySQL and creates tables at import time, so we
# stub those two calls out before importing it.
with mock.patch.object(peewee.MySQLDatabase, "connect", lambda self, *a, **kw: True), \
     mock.patch.object(peewee.MySQLDatabase, "create_tables", lambda self, *a, **kw: None):
    from app import app as flask_app
    from app import TimelinePost

TEST_MODELS = [TimelinePost]
test_db = peewee.SqliteDatabase(":memory:")


@pytest.fixture(autouse=True)
def isolated_db():
    with test_db.bind_ctx(TEST_MODELS):
        test_db.create_tables(TEST_MODELS)
        try:
            yield
        finally:
            test_db.drop_tables(TEST_MODELS)


@pytest.fixture
def app():
    flask_app.config.update(TESTING=True)
    return flask_app


@pytest.fixture
def client(app):
    return app.test_client()
