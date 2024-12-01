import pytest
import allure
import data


class TestCreateUser:

    @allure.title('Проверка создания нового пользователя')
    @allure.description('Создается юзер через Faker, проверяется код и тело ответа  ')
    def test_create_user_ok(self, create_and_delete_user):
        payload, response = create_and_delete_user
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Проверка создания пользователя повторно')
    @allure.description('Создается новый рандомный юзер, затем создается юзер с такими же данными')
    def test_create_exist_user(self,create_and_delete_user, user_methods):
        payload, response = create_and_delete_user
        new = user_methods.create_user(payload)
        assert new.status_code == 403 and new.json().get("message") == data.ALREADY_EXISTS

    @allure.title('Проверка создания пользователя с недостающими параметрами')
    @allure.description('Три попытки создать юзера с разными недостающими полями')
    @pytest.mark.parametrize("user_data", data.NOT_ALL_FIELDS )
    def test_create_user_without_required_fields(self, user_methods, user_data ):
        new = user_methods.create_user(user_data)
        assert new.status_code == 403 and new.json().get("message") == data.REQUIRED_FIELDS

