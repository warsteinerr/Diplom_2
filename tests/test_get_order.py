import pytest
import allure
import data
from helper import *


class TestGetOrder:

    @allure.title('Проверка получения списка заказов юзера')
    @allure.description('Создается рандомный юзер, ему добавляется заказ и запрашиваем его.')
    def test_get_list_of_orders_authorised(self, order_method, create_and_delete_user):
        payload, response1 = create_and_delete_user
        order_method.create_order_authorised(response1)
        response = order_method.get_list_of_orders_authorised(response1)
        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Проверка получения заказов без авторизации')
    @allure.description('Пытаемя отправить запрос на получение списка заказов без авторизации')
    def test_get_list_of_orders_unauthorised(self, order_method):
        response = order_method.get_list_of_orders_unauthorised()
        assert response.status_code == 401 and response.json().get("message") == data.AUTHORISATION_REQUIRED