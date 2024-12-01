from faker import Faker

def create_user_payload():
    fake = Faker()
    email = fake.free_email()
    name = email.split('@')[0]
    password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }
    return payload


def get_token(response):
    return response.json().get('accessToken')
