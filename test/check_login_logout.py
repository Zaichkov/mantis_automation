from fixture.session import SessionHelper


def test_login_logout(app):
    app.session.login('administrator', 'administrator')
    assert app.session.is_logged_in_as('administrator')
    app.session.logout()
    text = app.wd.find_element_by_css_selector('h4.header.lighter.bigger').text
    assert text == 'Вход'
