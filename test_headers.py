import requests


class TestHeader:
    def test_header_request(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)
        print(response.headers)

        assert response.status_code == 200, "Wrong response code"

        assert "x-secret-homework-header" in response.headers, "There is no header x-secret-homework-header1 in the " \
                                                                "headers"

        expected_header_value = 'Some secret value'
        actual_header_value = response.headers.get('x-secret-homework-header')
        assert actual_header_value == expected_header_value, "Actual header value in the response is not correct"
