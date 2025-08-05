import requests


class CompanyApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # Получить список компаний
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company/list', params=params_to_add)
        return resp.json()

    # Получить токен авторизации
    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]

    # Добавить компанию:
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        resp = requests.post(self.url + '/company/create',
                             json=company)
        return resp.json()
    

from CompanyApi import CompanyApi


api = CompanyApi("http://5.101.50.27:8000")

def test_get_companies():
    body = api.get_company_list()
    assert len(body)  > 0

# Проверка получения активных компаний
def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    assert len(full_list)  > len(filtered_list)

 # Проверка добавления новой компании
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = "Autotest"
    descr = "Descr"
    api.create_company(name, descr)

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr