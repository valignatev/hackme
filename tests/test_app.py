from flask import url_for
import pytest


@pytest.mark.usefixtures('live_server')
def test_google(selenium):
    selenium.get(url_for('hello', _external=True))
    assert 'fuckrkn' == selenium.title
