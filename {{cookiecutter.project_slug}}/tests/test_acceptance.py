import pytest

from {{cookiecutter.project_slug}} import app


@pytest.fixture
def client():
    """Test client for the app."""
    return app.test_client()


def test_index_view_should_return_OK(client):  # noqa
    rv = client.get('/')
    assert b'OK' in rv.data
