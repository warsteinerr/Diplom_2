import pytest
import allure
import data
from helper import *


class TestOrderMethods:
    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Пытаемся создать заказ без указания токена авторизации ')
    def test_create_order_unauthorised(self, order_method):
        response = order_method.create_order_unauthorised()
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Создаем заказ с указанием токена авторизации.')
    def test_create_order_authorised(self, order_method, create_and_delete_user):
        payload, response1 = create_and_delete_user
        response = order_method.create_order_authorised(response1)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Проверка создания заказа без ингридиентов')
    @allure.description('Пытаемся создать заказ авторизованным юзером, указав пустой список ингредиентов')
    def test_create_order_authorised_without_ingredients(self, order_method, create_and_delete_user):
        payload, response1 = create_and_delete_user
        response = order_method.create_order_authorised_without_ingredients(response1)
        assert response.status_code == 400 and response.json().get("message") == data.INGREDIENTS_REQUIRED

    @allure.title('Проверка некорректного хэша ингридентов')
    @allure.description('Пытмаемся создать заказ авторизованным юзером, указывае неправильный хэш ингредиентов')
    def test_create_order_authorised_incorrect_hash(self, order_method, create_and_delete_user):
        payload, response1 = create_and_delete_user
        response = order_method.create_order_authorised_incorrect_hash(response1)
        assert response.status_code == 400 and response.json().get("message") == data.INCORRECT_HASH

