import requests

# Объявляем переменную
resp_body = {}

def test_simple_req():
    global resp_body  # Указываем, что используем глобальную переменную
    
    try:
        # Выполняем запрос
        resp = requests.get('http://5.101.50.27:8000/company/list')
        
        # Проверяем статус
        assert resp.status_code == 200, f"Ожидался код 200, получен {resp.status_code}"
        
        # Получаем JSON
        resp_body = resp.json()
        
        return resp_body
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка при парсинге JSON: {e}")
        return None

# Вызываем функцию
test_simple_req()

# Теперь можно вывести результат
print(resp_body)