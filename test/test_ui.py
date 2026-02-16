import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from Main import Main

@pytest.mark.ui_test
@allure.title('Название книги на русском языке')
@allure.description('Тест проверяет, что поиск по названию книги на русском языке осуществляется корректно.')
@allure.feature('search')
@allure.severity('CRITICAL')
def test_search_russian_book_positive():
    with allure.step('Открыть страницу интернет магазина в браузере Chrome'):
        main_pages = Main(browser)
        main_pages.get_browser()

    with allure.step('Ввести в поле поиска название  на кириллице'):
        main_pages.get_search().send_keys('Хоббит')

    with allure.step('Кликнуть на поиск'):
        main_pages.click_botton_search()

    with allure.step('Проверить, что результатов поиска больше 0'):
        result = main_pages.search_results()
        assert result>0

    with allure.step('Закрыть браузер'):
        browser.quit()

@pytest.mark.ui_test
@allure.title('Название книги на английском языке')
@allure.description('Тест проверяет, что поиск по названию книги на английском языке осуществляется корректно.')
@allure.feature('search')
@allure.severity('CRITICAL')
def test_search_english_book_positive():
    with allure.step('Открыть страницу интернет магазина в браузере Chrome'):
        main_pages = Main(browser)
        main_pages.get_browser()

    with allure.step('Ввести в поле поиска название книги на латинице'):
        main_pages.get_search().send_keys('The Lord of the Rings')

    with allure.step('Кликнуть на поиск'):
        main_pages.click_botton_search()

    with allure.step('Проверить, что результатов поиска больше 0'):
        result = main_pages.search_results()
        assert result > 0

    with allure.step('Закрыть браузер'):
        browser.quit()

@pytest.mark.ui_test
@allure.title('Название книги из цифр')
@allure.description('Тест проверяет, что поиск по названию книги из цифр осуществляется корректно.')
@allure.feature('search')
@allure.severity('CRITICAL')
def test_search_numbers_book_positive():
    with allure.step('Открыть страницу интернет магазина в браузере Chrome'):
        main_pages = Main(browser)
        main_pages.get_browser()

    with allure.step('Ввести в поле поиска название книги из цифр'):
        main_pages.get_search().send_keys('1984')

    with allure.step('Кликнуть на поиск'):
        main_pages.click_botton_search()

    with allure.step('Проверить, что результатов поиска больше 0'):
        result = main_pages.search_results()
        assert result > 0

    with allure.step('Закрыть браузер'):
        browser.quit()

@pytest.mark.ui_test
@allure.title('Один символ')
@allure.description('Тест проверяет, что поиск книги по одному символу не осуществляется.')
@allure.feature('search')
@allure.severity('NORMAL')
def test_search_one_simbol_negative():
    with allure.step('Открыть страницу интернет магазина в браузере Chrome'):
        main_pages = Main(browser)
        main_pages.get_browser()

    with allure.step('Ввести в поле поиска название книги из одного символа'):
        main_pages.get_search().send_keys('я')

    with allure.step('Кликнуть на поиск'):
        main_pages.click_botton_search()

    with allure.step('Проверить, что всплыла ошибка'):
        result = main_pages.error()
        text_error = 'Похоже, у нас такого нет'
        assert result == text_error

    with allure.step('Закрыть браузер'):
        browser.quit()

@pytest.mark.ui_test
@allure.title('Специальные символы')
@allure.description('Тест проверяет, что поиск книги состоящей из спец символов не осуществляется.')
@allure.feature('search')
@allure.severity('NORMAL')
def test_search_special_simbols_negative():
    with allure.step('Открыть страницу интернет магазина в браузере Chrome'):
        main_pages = Main(browser)
        main_pages.get_browser()

    with allure.step('Ввести в поле поиска название книги из спец символов'):
        main_pages.get_search().send_keys('№%(*')

    with allure.step('Кликнуть на поиск'):
        main_pages.click_botton_search()

    with allure.step('Проверить, что всплыла ошибка'):
        result = main_pages.error()
        text_error = 'Похоже, у нас такого нет'
        assert result == text_error

    with allure.step('Закрыть браузер'):
        browser.quit()
