import allure
from selene import browser, have, be

from utils.logger import step


class MainPage:

    @allure.step("open browser")
    def open(self):
        browser.open("/")

    @step
    @allure.step("Search")
    def search_item_by_tool_number(self, value):
        browser.element('#partNumberSearch').should(be.blank).send_keys(value)
        browser.element('.search-button').click()
        browser.element('.breadcrumbs-header').should(have.text(value))

    @step
    @allure.step("Checking phrase")
    def main_page_should_have_visible_text(self):
        browser.element('.homepage-content__title').should(have.exact_text('Запчасти в интернет-магазине Автодок'))
