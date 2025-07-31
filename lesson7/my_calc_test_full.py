from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Инициализация драйвера Chrome (как указано в задании)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # 1. Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # 2. Установка задержки
    delay_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("1")
    
    # 3. Нажатие кнопок с проверкой их кликабельности
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".clear"))).click()   
  
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()   
    sleep(5)
    # 4. Ожидание результата ровно до 5 секунд
    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))).text
    sleep(1)
    print(f"Тест пройден успешно! Результат {result_element}")

except Exception as e:
    print(f"Ошибка во время выполнения теста: {str(e)}")
    driver.save_screenshot("lesson7\error.png")
    raise    

finally:
    driver.quit()