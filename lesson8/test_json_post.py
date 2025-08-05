import requests


base_url = "http://5.101.50.27:8000"

def test_create_company():
    
    # для авторизации создаем словарь с логином и паролем
    creds = {
        'username' : 'login',
        'password' : 'Gfhjkm#1'
    }

    # словарь для отправки информации, для создания события
    company = {
        "name": "ZOPA-MIRA",
        "description": "TESTtestTEST"
    }

    # авторизация
    resp = requests.post(base_url + '/auth/login', json=creds)
    # из полученного ответа в виде словаря, находим ключ "userToken" и записываем в переменную его значение (токен)
    token = resp.json()["userToken"]

    # переменная с токеном в виде словаря с ключом и значением в виде токена
    my_headers = {}
    my_headers["x-client-token"] = token

    # отправляем запрос на создание компании
    resp = requests.post(base_url + '/company/create', json=company)
    # можно записать альтернативно
    resp = requests.post(base_url + '/company/create', json={
        "name": "ZOPA-MIRA",
        "description": "TESTtestTEST"
    })
    assert resp.status_code == 201

test_create_company()