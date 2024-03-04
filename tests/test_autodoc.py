import pytest

from autodoc.pages.main_page import MainPage
from selene import browser
import time


def test_open_main_page():
    main_page = MainPage()
    main_page.open()
    main_page.search_item_by_tool_number('ZIC 132661')


def test_main_page_should_have_exact_visible_text():
    main_page = MainPage()
    main_page.open()
    main_page.main_page_should_have_visible_text()