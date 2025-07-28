from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера Firefox
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    # создаем словарь, в который записываем пары ключ-значение имя_поля:значение_поля
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    # далее с помощью цикла перебираем поля и находим необходимые и заносим в них значения
    for field_name, value in fields.items():
        element = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
        element.clear()
        element.send_keys(value)

    # Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    
    # Ожидание применения стилей
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.py-2.alert-danger")))
    
    # Проверка подсветки Zip code (красный)
    zip_code = driver.find_element(By.NAME, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class"), "Zip code не подсвечен красным"
    
    # Проверка подсветки остальных полей (зеленый)
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    
    for field_name in fields_to_check:
        field = driver.find_element(By.NAME, field_name)
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_name} не подсвечено зеленым"
    
    print("Все проверки пройдены успешно!")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
    raise  # Перебрасываем исключение дальше, чтобы увидеть детали ошибки

finally:
    driver.quit()