import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    # Установка задержки
    delay_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("1")
    return driver

def clear_calculator(calculator):
    WebDriverWait(calculator, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".clear"))).click()

def test_addition(calculator):
    """Тест на сложение"""
    clear_calculator(calculator)
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        WebDriverWait(calculator, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()
    
    result = WebDriverWait(calculator, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    assert result, "Результат сложения неверный"

def test_subtraction(calculator):
    """Тест на вычитание"""
    clear_calculator(calculator)
    buttons = ["9", "-", "4", "="]
    for button in buttons:
        WebDriverWait(calculator, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()
    
    result = WebDriverWait(calculator, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "5"))
    assert result, "Результат вычитания неверный"

def test_multiplication(calculator):
    """Тест на умножение"""
    clear_calculator(calculator)
    buttons = ["3", "x", "5", "="]
    for button in buttons:
        WebDriverWait(calculator, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()
    
    result = WebDriverWait(calculator, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    assert result, "Результат умножения неверный"

def test_division(calculator):
    """Тест на деление"""
    clear_calculator(calculator)
    buttons = ["8", "÷", "2", "="]
    for button in buttons:
        WebDriverWait(calculator, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()
    
    result = WebDriverWait(calculator, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "4"))
    assert result, "Результат деления неверный"

def test_clear_button(calculator):
    """Тест кнопки очистки"""
    # Вводим число
    WebDriverWait(calculator, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
    # Очищаем
    WebDriverWait(calculator, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".clear"))).click()
    
    result = WebDriverWait(calculator, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))).text
    assert result == "", f"Ожидался пустой результат, получено {result}"