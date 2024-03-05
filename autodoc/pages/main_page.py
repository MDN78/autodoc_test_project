import allure
from selene import browser, have, be
from autodoc.data.users import User
from utils.logger import step


class MainPage:

    @step
    @allure.step("open browser")
    def open(self):
        browser.open("/")

    @step
    @allure.step('Authorization registered user')
    def authorization_registered_user(self, user: User):
        browser.element('#loginInfo').click()
        browser.element('#Login').should(be.blank).send_keys(user.username)
        browser.element('#Password').should(be.blank).send_keys(user.password)
        browser.element('.icon.fa').click()
        browser.element('#submit_logon_page').click()
        browser.element('#user_info').should(have.exact_text(user.username))

    @step
    @allure.step('Authorization unregistered user')
    def authorization_unregistered_user(self, user: User):
        browser.element('#loginInfo').click()
        browser.element('#Login').should(be.blank).send_keys(user.username)
        browser.element('#Password').should(be.blank).send_keys(user.password)
        browser.element('.icon.fa').click()
        browser.element('#submit_logon_page').click()
        browser.element('#errorMessage').should(have.exact_text('Не удалось авторизоваться.'))


    # @step
    # @allure.step('Authorization')
    # def authorization(self, name, password):
    #     browser.element('#loginInfo').click()
    #     browser.element('#Login').should(be.blank).send_keys(name)
    #     browser.element('#Password').should(be.blank).send_keys(password)
    #     browser.element('.icon.fa').click()
    #     browser.element('#submit_logon_page').click()
    #     browser.element('#user_info').should(have.exact_text(name))


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
