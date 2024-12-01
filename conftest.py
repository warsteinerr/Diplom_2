import data
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

import pytest
from faker import Faker
import requests


@pytest.fixture
def user_methods():
    return UserMethods()

@pytest.fixture()
def order_method():
    return OrderMethods()


@pytest.fixture()
def create_and_delete_user():
    fake = Faker()
    email = fake.free_email()
    name = fake.first_name()
    password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }
    response = requests.post(f'{data.BASE_URL}{data.USER_CREATE_URL}', json=payload)
    yield payload, response
    access_token = response.json().get('accessToken')
    requests.delete(f'{data.BASE_URL}{data.DELETE_USER_URL}', headers={'Authorization': access_token})