BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
USER_CREATE_URL = "auth/register"
DELETE_USER_URL = "auth/user"
LOGIN_URL = "auth/login"
UPDATE_URL = "auth/user"
CREATE_ORDER_URL = "orders"
GET_LIST = "orders"


ALREADY_EXISTS = "User already exists"
REQUIRED_FIELDS = "Email, password and name are required fields"
INCORRECT_LOGIN_DATA = "email or password are incorrect"
INGREDIENTS_REQUIRED = "Ingredient ids must be provided"
INCORRECT_HASH = "One or more ids provided are incorrect"
AUTHORISATION_REQUIRED = "You should be authorised"

NOT_ALL_FIELDS = [
    {'email': '',
     'password': 'qqqqqqqq',
     'name': 'Qqqq'
     },
    {'email': 'qqqqq@gmail.com',
     'password': '',
     'name': 'Qqqq'
     },
    {'email': 'qqqqq@gmail.com',
     'password': 'qqqqqqqq',
     'name': ''
     }
]

INGRIDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]
INGRIDIENTS_WRONG = ["63c0c5a71d1f82001bdaaa6d", "63c0c5a71d1f82001bdaaa6f", "63c0c5a71d1f82001bdaaa70"]