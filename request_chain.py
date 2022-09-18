import requests
import time

response1 = requests.post("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response1.text)
parsed_response_text1 = response1.json()
print(parsed_response_text1["token"])

payload = {"token": parsed_response_text1["token"]}

response2 = requests.post("https://playground.learnqa.ru/ajax/api/longtime_job", data=payload)
parsed_response_text2 = response2.json()
print(parsed_response_text2["status"])

if parsed_response_text2["status"] == "Job is NOT ready":
    time.sleep(parsed_response_text1["seconds"])
    response3 = requests.post("https://playground.learnqa.ru/ajax/api/longtime_job", data=payload)
    parsed_response_text3 = response3.json()
    print(parsed_response_text3["status"])
    print(parsed_response_text3["result"])
    assert parsed_response_text3["status"] == "Job is ready"
    assert parsed_response_text3["result"]
else:
    print("Поле status первого запроса имеет некорректное значение или задача уже выполнена")
