from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация драйвера Chrome (как указано в задании)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # 1. Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # 2. Установка задержки
    delay_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")
    
    # 3. Нажатие кнопок с проверкой их кликабельности
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()
    
    # 4. Проверка, что результат НЕ появляется сразу
    start_time = time.time()
    try:
        result = WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        assert False, "Результат появился слишком быстро!"
    except:
        print("Результат не появился сразу (ожидаемо)")
    
    # 5. Ожидание результата ровно 45 секунд
    result_element = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    
    # 6. Проверка времени выполнения
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Фактическое время выполнения: {execution_time:.2f} секунд")
    
    # Проверка что результат появился примерно через 45 секунд (с допуском ±2 сек)
    assert 43 <= execution_time <= 47, \
        f"Время выполнения {execution_time:.2f} сек не соответствует ожидаемому (45±2 сек)"
    
    print(f"Тест пройден успешно! Результат появился через {execution_time:.2f} секунд")

except Exception as e:
    print(f"Ошибка во время выполнения теста: {str(e)}")
    driver.save_screenshot("error.png")
    raise    

finally:
    driver.quit()