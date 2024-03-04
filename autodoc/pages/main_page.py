# # import allure
from selene import browser, have, be
# # from selene.core import command
# # from utils.logger import step
# # # from demoqa_tests import resource
#
#
class MainPage:

    # @step
    # @allure.step('Open maim page')
    def open(self):
        browser.open("/")
        # # удаление рекламы - предусловие тестового сценария
        # browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
        #     have.size_greater_than_or_equal(3)
        # )
        # browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)
        # # checking modal window
        # if browser.element('[aria-label="Consent"]').matching(be.visible):
        #     browser.element('[aria-label="Consent"]').click()
    def search_item_by_tool_numder(self, value):
        browser.element('#partNumberSearch').should(be.blank).send_keys(value)
        browser.element('.search-button').click()

    def main_page_should_have_visible_text(self):
        browser.element('.homepage-content__title').should(have.exact_text('Запчасти в интернет-магазине Автодок'))