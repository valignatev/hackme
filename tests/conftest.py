import pytest

from shoppy.app import app as shoppy_app


@pytest.fixture
def app():
    return shoppy_app
