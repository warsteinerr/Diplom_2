import pytest
import allure
import data


class TestUserLogin:
    @allure.title('Проверка уcпешной авторизации нового пользователя')
    @allure.description('Создаем рандомного юзера и авторизуемся под ним')
    def test_new_user_login(self, user_methods, create_and_delete_user):
        payload, response1 = create_and_delete_user
        response = user_methods.login_user(payload)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Проверка авторизации с неверной почтой')
    @allure.description('Создаем юзера, подменяем ему почту и пытаемся залогиниться')
    def test_incorrect_mail_login(self, user_methods, create_and_delete_user):
        payload, response1 = create_and_delete_user
        response = user_methods.login_incorrect_mail(payload)
        assert response.status_code == 401 and response.json().get("message") == data.INCORRECT_LOGIN_DATA

    @allure.title('Проверка авторизации с неверным паролем')
    @allure.description('Создаем юзера, подменяем ему пароль и пытаемся залогиниться')
    def test_incorrect_password_login(self, user_methods, create_and_delete_user):
        payload, response1 = create_and_delete_user
        response = user_methods.login_incorrect_password(payload)
        assert response.status_code == 401 and response.json().get("message") == data.INCORRECT_LOGIN_DATA



