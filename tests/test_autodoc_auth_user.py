import os

import pytest

from autodoc.data.users import User
from autodoc.pages.main_page import MainPage


@pytest.mark.skip
def test_authorization_registered_user():
    main_page = MainPage()
    main_page.open()
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    main_page.authorization_registered_user(registered_user)
