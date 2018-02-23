from shoppy.app import hello


def test_add():
    assert hello() == 'Sup XSS'
