import random
import string

import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):
    exclude_fields = [
        ("no_password"),
        ("no_username"),
        ("no_firstName"),
        ("no_lastName"),
        ("no_email")
    ]

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        self.incorrect_email = f"{base_part}{random_part}{domain}"


    def test_create_user_successfully(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email,
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email,
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.incorrect_email,
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "Invalid email format", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('condition', exclude_fields)
    def test_create_user_without_any_field(self, condition):

        if condition == "no_password":
            response = requests.post('https://playground.learnqa.ru/api/user/', data={'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': self.email})
        elif condition == "no_username":
            response = requests.post('https://playground.learnqa.ru/api/user/', data={'password': '1234', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': self.email})
        elif condition == "no_firstName":
            response = requests.post('https://playground.learnqa.ru/api/user/', data={'password': '1234', 'username': 'learnqa', 'lastName': 'learnqa', 'email': self.email})
        elif condition == "no_lastName":
            response = requests.post('https://playground.learnqa.ru/api/user/', data={'password': '1234', 'username': 'learnqa', 'firstName': 'learnqa', 'email': self.email})
        else:
            response = requests.post('https://playground.learnqa.ru/api/user/', data={'password': '1234', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'})

        field_name = condition.split('_')

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
          "utf-8") == f"The following required params are missed: {field_name[1]}", f"Unexpected response content {response.content}"

    def test_create_user_with_long_name(self):
        length = random.randint(251, 1000)
        firstName = ''.join(random.choices(string.ascii_letters, k=length))
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': firstName,
            'lastName': 'learnqa',
            'email': self.email,
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
         "utf-8") == "The value of 'firstName' field is too long", f"Unexpected response content {response.content}"

    def test_create_user_with_short_name(self):
        firstName = ''.join(random.choices(string.ascii_letters, k=1))
        data = {
                'password': '1234',
                'username': 'learnqa',
                'firstName': firstName,
                'lastName': 'learnqa',
                'email': self.email,
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
                "utf-8") == "The value of 'firstName' field is too short", f"Unexpected response content {response.content}"




