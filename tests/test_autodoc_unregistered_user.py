import os
from autodoc.data.users import User
from autodoc.pages.main_page import MainPage


def test_authorization_unregistered_user():
    main_page = MainPage()
    main_page.open()
    unregistered_user = User(
        username=os.getenv('UNREGISTERED_USER_LOGIN'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )
    main_page.authorization_unregistered_user(unregistered_user)
