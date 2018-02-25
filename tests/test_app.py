from flask import url_for
import pytest


@pytest.mark.usefixtures('live_server')
def test_catalog(selenium):
    selenium.get(url_for('catalog', _external=True))
    assert 3 == len(selenium.find_elements_by_class_name('product'))
