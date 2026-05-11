import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
load_dotenv()


class Main:
    """
    Этот класс представляет главную страницу интернет-магазина. У страницы есть поле поиска
    И страницу с результатами поиска
    """
    def __init__(self, browser):
        self.driver = browser

        url = os.getenv("URL")
        self.url = url

    @allure.step('Открыть страницу интернет-магазина в браузере Chrome ')
    def get_browser(self) -> None:
        """
        Эта функция открывает страницу интернет-магазина в Chrome
        """
        self.driver.get(self.url)

    @allure.step('Найти строку поиска')
    def get_search(self) -> WebElement:
        """
        Эта функция находит строку поиска
        """
        search = self.driver.find_element(By.CSS_SELECTOR, '#app-search')
        return search

    @allure.step('Кликнуть на кнопку поиска')
    def click_botton_search(self) -> None:
        """
        Эта функция кликает на кнопку поиска
        """
        self.driver.find_element(By.CSS_SELECTOR, '.search-form__button-search').click()

    @allure.step('Результат удачного поиска')
    def search_results(self) -> int:
        """
        Эта функция отображает какое количество товаров было найдено
        Возвращает число
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.catalog-products-total')))

        results = self.driver.find_element(By.CSS_SELECTOR, '.catalog-products-total').text
        results = results.replace(' товаров', '')
        return int(results)

    @allure.step('Результат неудачного поиска')
    def error(self) -> str:
        """
        Эта функция отображает ошибку при некорректном поиске
        Возвращает текст ошибки
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.catalog-stub__title')))

        results = self.driver.find_element(By.CSS_SELECTOR, '.catalog-stub__title').text
        return results
