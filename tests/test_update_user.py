import pytest
import allure
import data
from helper import *


class TestUpdateUser:

    @allure.title('Проверка обновления данных юзера')
    @allure.description('Создаем двух юзеров поочередно, Присваиваем данные второго второго первому ')
    def test_update_user(self, create_and_delete_user, user_methods):
        payload1, response1 = create_and_delete_user
        payload = create_user_payload()
        response = user_methods.update_authorised_user(payload, response1)
        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Проверка обновления данных неавторизованного юзера')
    @allure.description('Создаем рандомного юзера, но не авторизуемся. Пытаемся обновить его данные')
    def test_update_unaauthorised_user(self, user_methods):
        payload = create_user_payload()
        response = user_methods.update_unauthorised_user(payload)
        assert response.status_code == 401 and response.json().get('success') is False

