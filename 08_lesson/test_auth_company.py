import requests
import json
from pathlib import Path

# константы
HEADER = {'Authorization': 'Bearer 1754393725260_a4ff66abe53ed0d61bc4913f9dd3981bbbdac0e1090868a1f042ecbd3a2e8a7f',
          'Content-Type': 'application/json'}
BASE_URL = 'https://ru.yougile.com/api-v2'
LOGIN = "only-max@yandex.ru"
PASSWORD = "FRHRG7LT"
NAME = "Maxim"

# словарь с телом запроса
auth_creds = {
        'login' : LOGIN,
        'password' : PASSWORD,
        'name' : NAME
    }

# пустой словарь, чтобы в него позже записать ответ
resp_body = {}

def test_auth():
    global resp_body
    auth_response = requests.post(
    f"{BASE_URL}/auth/companies", json=auth_creds)

    # Проверка статуса ответа
    if auth_response.status_code == 200:
        print("Успешно! Ответ:", auth_response.json())
        resp_body = auth_response.json()
        return resp_body
    else:
        print("Ошибка:", auth_response.status_code, auth_response.text)

# Получаем данные
data_auth = test_auth()

# Сохраняем в файл как текст
if data_auth:
    with open('08_lesson/data_auth.txt', 'w', encoding='utf-8') as file:
        file.write(str(data_auth))
    print("Данные успешно сохранены в файл data_auth.txt")