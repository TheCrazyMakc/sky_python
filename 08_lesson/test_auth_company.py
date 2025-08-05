import requests

HEADER = {'Authorization': 'Bearer 1754393725260_a4ff66abe53ed0d61bc4913f9dd3981bbbdac0e1090868a1f042ecbd3a2e8a7f',
          'Content-Type': 'application/json'}
BASE_URL = 'https://ru.yougile.com/api-v2'

LOGIN = "only-max@yandex.ru"
PASSWORD = "FRHRG7LT"
NAME = "Maxim"

auth_creds = {
        'login' : LOGIN,
        'password' : PASSWORD,
        'name' : NAME
    }

resp_body = {}

def test_auth():
    global resp_body
    auth_response = requests.post(
    "https://ru.yougile.com/api-v2/auth/companies", json=auth_creds)

    # Проверка статуса ответа
    if auth_response.status_code == 200:
        print("Успешно! Ответ:", auth_response.json())
        resp_body = auth_response.json()
        return resp_body
    else:
        print("Ошибка:", auth_response.status_code, auth_response.text)

# Получаем данные
data_get = test_auth()

# Сохраняем в файл как текст
if data_get:
    with open('08_lesson/data_get.txt', 'w', encoding='utf-8') as file:
        file.write(str(data_get))
    print("Данные успешно сохранены в файл data_get.txt")