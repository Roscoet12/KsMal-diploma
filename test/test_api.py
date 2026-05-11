import pytest
import allure
import os
from dotenv import load_dotenv
load_dotenv()

from CardApi import CardApi

api_url = os.getenv("API_URL")

api = CardApi(api_url)


@pytest.mark.api_test
@allure.title('Добавить книгу в корзину')
@allure.description('Тест проверяет, книга по id добавляется в корзину корректно.')
@allure.feature('card')
@allure.severity('CRITICAL')
def test_add_book():
    with allure.step('Добавить книгу в корзину с валидным id'):
        id_book = 2558779
        result = api.add_book(id_book)

    with allure.step('Проверить статус-код запроса'):
        assert result.status_code == 200

    with allure.step('Найти динамическую id'):
        id_book = api.id_book()
        new_id_book = str(id_book['products'][0]['id'])

    with allure.step('Удалить добавленную книгу'):
        api.delete_book(new_id_book)

@pytest.mark.api_test
@allure.title('Увеличить количество книг в корзине')
@allure.description('Тест проверяет, в корзине можно добавить еще одну книгу по id.')
@allure.feature('card')
@allure.severity('CRITICAL')
def test_increase_book():
    with allure.step('Добавить книгу в корзину с валидным id'):
        id_book = 2558779
        api.add_book(id_book)

    with allure.step('Найти динамическую id'):
        id_book = api.id_book()
        new_id_book = id_book['products'][0]['id']

    with allure.step('Увеличить количество книг в корзине'):
        result = api.increase_book(new_id_book, 3)

    with allure.step('Проверить статус-код запроса'):
        assert result.status_code == 200

    with allure.step('Удалить добавленную книгу'):
        api.delete_book(str(new_id_book))

@pytest.mark.api_test
@allure.title('Удалить книгу из корзины')
@allure.description('Тест проверяет, книга удаляется из корзины корректно.')
@allure.feature('card')
@allure.severity('CRITICAL')
def test_delete_book():
    with allure.step('Добавить книгу в корзину с валидным id'):
        id_book = 2558779
        api.add_book(id_book)

    with allure.step('Найти динамическую id'):
        id_book = api.id_book()
        new_id_book = str(id_book['products'][0]['id'])

    with allure.step('Удалить добавленную книгу'):
        result = api.delete_book(new_id_book)

    with allure.step('Проверить статус-код запроса'):
        assert result.status_code == 204

@pytest.mark.api_test
@allure.title('Добавить несуществующую книгу в корзину')
@allure.description('Тест проверяет, нельзя добавить книгу с несуществующим id.')
@allure.feature('card')
@allure.severity('NORMAL')
def test_add_non_existent_book():
    with allure.step('Добавить книгу в корзину с невалидным id'):
        id_book = 8745678
        result = api.add_book(id_book)

    with allure.step('Проверить статус-код запроса'):
        assert result.status_code == 400

@pytest.mark.api_test
@allure.title('Удалить книгу из пустой корзины')
@allure.description('Тест проверяет, нельзя удалить книгу из пустой корзины.')
@allure.feature('card')
@allure.severity('NORMAL')
def test_delete_none_book():
    with allure.step('Добавить книгу в корзину с валидным id'):
        id_book = 2558779
        api.add_book(id_book)

    with allure.step('Найти динамическую id'):
        id_book = api.id_book()
        new_id_book = str(id_book['products'][0]['id'])

    with allure.step('Удалить добавленную книгу'):
        api.delete_book(new_id_book)

    with allure.step('Удалить книгу из пустой корзины'):
        result = api.delete_book(new_id_book)

    with allure.step('Проверить статус-код запроса'):
        assert result.status_code == 404
