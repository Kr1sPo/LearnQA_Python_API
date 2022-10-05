import random
import string
from lib.my_requests import MyRequests
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

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post('user/', data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post('user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        incorrect_email = "learnqaexample.com"
        data = self.prepare_registration_data(incorrect_email)

        response = MyRequests.post('user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "Invalid email format", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('condition', exclude_fields)
    def test_create_user_without_any_field(self, condition):
        data = self.prepare_registration_data(None, condition)
        response = MyRequests.post('user/', data=data)

        field_name = condition.split('_')

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
          "utf-8") == f"The following required params are missed: {field_name[1]}", f"Unexpected response content {response.content}"

    def test_create_user_with_long_name(self):
        length = random.randint(251, 1000)
        firstName = ''.join(random.choices(string.ascii_letters, k=length))
        data = self.prepare_registration_data(None, None, firstName)

        response = MyRequests.post('user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
         "utf-8") == "The value of 'firstName' field is too long", f"Unexpected response content {response.content}"

    def test_create_user_with_short_name(self):
        firstName = ''.join(random.choices(string.ascii_letters, k=1))
        data = self.prepare_registration_data(None, None, firstName)

        response = MyRequests.post('user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
                "utf-8") == "The value of 'firstName' field is too short", f"Unexpected response content {response.content}"




