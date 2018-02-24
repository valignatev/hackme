from flask import url_for
import pytest


@pytest.mark.usefixtures('live_server')
def test_google(selenium):
    selenium.get(url_for('catalog', _external=True))
    assert 'Shoppy catalog' == selenium.title
