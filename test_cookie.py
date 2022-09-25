import requests


class TestCookie:
    def test_cookie_request(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        print(dict(response.cookies))

        assert response.status_code == 200, "Wrong response code"

        assert "HomeWork" in response.cookies, "There is no field HomeWork in the cookies"

        expected_cookies_value = 'hw_value'
        actual_cookies_value = response.cookies.get('HomeWork')
        assert actual_cookies_value == expected_cookies_value, "Actual cookies value in the response is not correct"
