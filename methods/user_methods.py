import allure
import requests
from faker import Faker
import data
from data import *
from helper import *


class UserMethods:

    @allure.step('Создаем нового юзера')
    def create_user(self, payload):
        response = requests.post(f'{data.BASE_URL}{data.USER_CREATE_URL}', json=payload)
        return response


    @allure.step("Логинимся юзером")
    def login_user(self, payload):
        return requests.post(f'{data.BASE_URL}{data.LOGIN_URL}', json={
            "email": payload["email"],
            "password": payload["password"]
        })

    @allure.step("Логинимся юзером с некорректной почтой")
    def login_incorrect_mail(self, payload):
        fake = Faker()
        return requests.post(f'{data.BASE_URL}{data.LOGIN_URL}', json={
            "email": fake.free_email(),
            "password": payload["password"]
        })
    @allure.step("Логинимся юзером с некорректным паролем")
    def login_incorrect_password(self, payload):
        fake = Faker()
        return requests.post(f'{data.BASE_URL}{data.LOGIN_URL}', json={
            "email": payload["email"],
            "password": fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        })


    @allure.step("Получение токена и обновление авторизованного пользователя ")
    def update_authorised_user(self, payload, response):
        access_token = get_token(response)
        response = requests.patch(
            f'{data.BASE_URL}{data.UPDATE_URL}',
            headers={
            'Authorization': f'{access_token}'
        },
            json=payload
        )
        return response

    @allure.step("Обновление неавторизованного пользователя")
    def update_unauthorised_user(self, payload):
        response = requests.patch(
            f'{data.BASE_URL}{data.UPDATE_URL}',
            headers={
        },
            json=payload
        )
        return response
