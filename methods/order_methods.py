import data
import allure
import requests
from helper import  *


class OrderMethods:
    @allure.step('Создание заказаза неавторизованным пользователем с ингридиентами')
    def create_order_unauthorised(self):
        response = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_URL}', json={'ingredients': data.INGRIDIENTS}, headers={})
        return response

    @allure.step('Создание заказаза авторизованным пользователем с ингридиентами')
    def create_order_authorised(self, response_fixture):
        token = get_token(response_fixture)
        return requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_URL}', json={'ingredients': data.INGRIDIENTS}, headers={'Authorization': f'{token}'})

    @allure.step('Создание заказаза авторизованным пользователем без ингридиенnов')
    def create_order_authorised_without_ingredients(self, response_fixture):
        token = get_token(response_fixture)
        return requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_URL}', json={'ingredients': []}, headers={'Authorization': f'{token}'})

    @allure.step('Создание заказа с неверным хэшем ингридиентов')
    def create_order_authorised_incorrect_hash(self, response_fixture):
        token = get_token(response_fixture)
        return requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_URL}', json={'ingredients': data.INGRIDIENTS_WRONG}, headers={'Authorization': f'{token}'})

    @allure.step('Получение списка заказов авторизованного юзера')
    def get_list_of_orders_authorised(self, response_fixture):
        token = get_token(response_fixture)
        return requests.get(f'{data.BASE_URL}{data.GET_LIST}', headers={'Authorization': f'{token}'})

    @allure.step('Получение списка заказов неавторизованного юзера')
    def get_list_of_orders_unauthorised(self):
        return requests.get(f'{data.BASE_URL}{data.GET_LIST}')


