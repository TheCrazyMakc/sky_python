from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Инициализация драйвера Edge
# driver = webdriver.Edge(
#     service=EdgeService(EdgeChromiumDriverManager().install()))

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    input_first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    input_first_name.send_keys("Иван")

    input_last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    input_last_name.send_keys("Петров")

    input_address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    input_address.send_keys("Ленина, 55-3")

    input_email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    input_email.send_keys("test@skypro.com")

    input_phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    input_phone_number.send_keys("+7985899998787")

    input_zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    input_zip_code.send_keys("") # сделать clear

    input_city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    input_city.send_keys("Москва")

    input_country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    input_country.send_keys("Россия")

    input_job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    input_job_position.send_keys("QA")

    input_company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    input_company.send_keys("SkyPro")

    search_button_login = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    search_button_login.click()    
 
    # Ожидание применения стилей
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.py-2.alert-danger")))
    # .alert — базовый класс алерта
    # .py-2 — класс для отступов
    # .alert-danger — класс для отображения опасного (красного) алерта
    
    # Проверка подсветки Zip code (красный)
    zip_code = driver.find_element(By.NAME, "zip-code")

    assert "alert-danger" in zip_code.get_attribute("class"), "Zip code не подсвечен красным"
    # Сообщение “Zip code не подсвечен красным” выводится при неудаче
    
    # Проверка подсветки остальных полей (зеленый)
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    
    for field_name in fields_to_check:
        field = driver.find_element(By.NAME, field_name)
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_name} не подсвечено зеленым"
    
    print("Все проверки пройдены успешно!")

finally:
    driver.quit()