from CompanyTable import CompanyTable

api = CompanyApi("")
db = CompanyTable("")

def test_get_companies():
  # получить список через api
  api_result = api.get_company_list()

  # получить список БД
  db_result = db.get_companies()

  # проверить что списки равны
  assert len(api_result) == len(db_result)

