import requests

# Case 1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

# Case 2
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
print(response.status_code)

# Case 3
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
print(response.text)
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
print(response.text)
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})
print(response.text)

# Case 4
request_types = ["GET", "POST", "PUT", "DELETE"]
methods = ["GET", "POST", "PUT", "DELETE"]

for i in range(len(request_types)):
    for k in range(len(methods)):
        payload = {"method": methods[k]}
        if request_types[i] == "GET":
            response = requests.request(request_types[i], "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                        params=payload)
        else:
            response = requests.request(request_types[i], "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                        data=payload)
        print(f"Пара {[i]} {request_types[i]} + {[k]} {methods[k]}")
        print(response.text)
