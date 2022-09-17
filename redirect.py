import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
history = response.history

number_of_redirects = len(history)+1

first_response = response.history[0]
second_response = response.history[1]
third_response = response

print(history)
print(number_of_redirects)
print(first_response.url)
print(second_response.url)
print(third_response.url)