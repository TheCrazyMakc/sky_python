import requests

resp_body = {}

def test_simple_req():
    global resp_body
    try:
        resp = requests.get('http://5.101.50.27:8000/company/list')
        assert resp.status_code == 200
        resp_body = resp.json()
        return resp_body
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Получаем данные
data = test_simple_req()

# Сохраняем в файл как текст
if data:
    with open('lesson8/data.txt', 'w', encoding='utf-8') as file:
        file.write(str(data))
    print("Данные успешно сохранены в файл data.txt")
