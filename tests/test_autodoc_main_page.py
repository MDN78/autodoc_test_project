import os
from autodoc.pages.main_page import MainPage
from autodoc.data.cars import Car


def test_registration_form_should_have_exact_visible_text():
    main_page = MainPage()
    main_page.open()
    main_page.registration_form_should_have_exact_visible_text()


def test_search_form_by_item_number():
    main_page = MainPage()
    main_page.open()
    main_page.search_item_by_tool_number('ZIC 132661')


def test_main_page_should_have_exact_visible_text():
    main_page = MainPage()
    main_page.open()
    main_page.main_page_should_have_visible_text()


def test_search_by_vin_number():
    main_page = MainPage()
    main_page.open()
    current_car = Car(
        vin=os.getenv('VIN_NUMBER')
    )
    main_page.search_by_vin_number(current_car)
