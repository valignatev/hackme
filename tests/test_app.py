from flask import url_for
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

pytestmark = pytest.mark.usefixtures('live_server')


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    return selenium


def test_catalog(selenium):
    selenium.get(url_for('catalog', _external=True))
    selenium.find_element_by_tag_name('input').send_keys('t', Keys.ENTER)
    assert 2 == len(selenium.find_elements_by_class_name('product'))


def test_no_xss(selenium):
    selenium.get(url_for('catalog', _external=True))
    selenium.find_element_by_tag_name('input').send_keys(
        '<script>alert()</script>',
        Keys.ENTER,
    )
    with pytest.raises(TimeoutException):
        WebDriverWait(selenium, 1).until(EC.alert_is_present())


def test_no_link_xss(selenium):
    selenium.get(url_for('product', product_id=1, _external=True))
    selenium.find_element_by_tag_name('textarea').send_keys(
        '<a href="javascript:alert()">click</a>',
        Keys.ENTER,
    )
    selenium.find_element_by_name('submit').click()
    selenium.find_element_by_link_text('click').click()
    with pytest.raises(TimeoutException):
        WebDriverWait(selenium, 1).until(EC.alert_is_present())
    assert 'Not Found' in selenium.page_source
