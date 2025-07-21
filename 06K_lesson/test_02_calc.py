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
import time

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Инициализация драйвера Edge
# driver = webdriver.Edge(
#     service=EdgeService(EdgeChromiumDriverManager().install()))

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
    
    # WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
    
    # WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
    
    # WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()

    buttons = ["7", "+", "8", "="]
    for button in buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()        
   
    # Ожидание появления результата с учетом задержки
    result_element = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # Проверка результата
    # result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    # assert result == "15", f"Ожидался результат 15, получено {result}"
    result_element = WebDriverWait(driver, 45).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen")))
    actual_result = result_element.text
    expected_result = "15"
    if actual_result == expected_result:
        print(f"Тест пройден успешно!")
    assert actual_result == expected_result, \
        f"Ошибка в калькуляторе: {actual_result} != {expected_result}"    

finally:
    driver.quit()