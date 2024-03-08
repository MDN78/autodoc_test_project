import os

import allure
import pytest
from allure_commons.types import Severity
from autodoc.data.users import User
from autodoc.pages.main_page import MainPage


@allure.tag('Autodoc')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'User')
@allure.feature('Authorization')
@allure.story('Auth registered user')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
@pytest.mark.skip
def test_authorization_registered_user():
    main_page = MainPage()
    main_page.open()
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    main_page.authorization_registered_user(registered_user)
