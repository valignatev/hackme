from flask import url_for
import pytest
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    return selenium


@pytest.mark.usefixtures('live_server')
def test_catalog(selenium):
    selenium.get(url_for('catalog', _external=True))
    selenium.find_element_by_tag_name('input').send_keys('t', Keys.ENTER)
    assert 2 == len(selenium.find_elements_by_class_name('product'))
