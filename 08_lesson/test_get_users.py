import requests

headers = {
    'Authorization': 'Bearer 1754393725260_a4ff66abe53ed0d61bc4913f9dd3981bbbdac0e1090868a1f042ecbd3a2e8a7f',
    'Content-Type': 'application/json'
}

response = requests.get('https://ru.yougile.com/api-v2/users', headers=headers)
print(response.json())
# print("Ошибка:", response.status_code, response.text)