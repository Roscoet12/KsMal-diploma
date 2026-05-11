import requests
import allure
from requests import Response
import os
from dotenv import load_dotenv
load_dotenv()


class CardApi:
    """
    Этот класс представляет Api запросы в корзине интернет-магазина
    """
    def __init__(self, url):
        self.url = url

        token = os.getenv("TOKEN")
        self.token = token

    @allure.step('Добавить книгу в корзину')
    def add_book(self, id: int) -> Response:
        """
        Эта функция добавляет книгу в корзину
        """
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        creds = {
            'id': id
        }
        resp = requests.post(self.url+'/product', json=creds, headers=headers)
        return resp

    @allure.step('Найти динамическую id')
    def id_book(self) -> dict:
        """
        Эта функция находит новый приcвоенный id.
        Так как id является динамической переменной, необходима для остальных запросов.
        """
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url, headers=headers)
        return resp.json()

    @allure.step('Удалить книгу из корзины')
    def delete_book(self, id_book) -> Response:
        """
        Эта функция удаляет книгу из корзины.
        Необходима динамическая id
        """
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.delete(self.url + '/product/' + id_book, headers=headers)
        return resp

    @allure.step('Увеличить количество книг в корзине')
    def increase_book(self, id: int, quantity: int) -> Response:
        """
        Эта функция увеличивает количество товара в корзине
        Необходима динамическая id
        Принимает значения id товара и количество товара
        """
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        creds = {
            'id': id,
            'quantity': quantity
        }
        resp = requests.put(self.url, json=creds, headers=headers)
        return resp
