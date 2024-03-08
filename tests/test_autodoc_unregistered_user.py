import os
import allure

from autodoc.data.users import User
from autodoc.pages.main_page import MainPage
from allure_commons.types import Severity


@allure.tag('Autodoc')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'User')
@allure.feature('Authorization')
@allure.story('Auth unregistered user')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_authorization_unregistered_user():
    main_page = MainPage()
    main_page.open()
    unregistered_user = User(
        username=os.getenv('UNREGISTERED_USER_LOGIN'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )
    main_page.authorization_unregistered_user(unregistered_user)
