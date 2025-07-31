from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from calc_test_class import CalculatorPage

def test_slow_calculator():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator = CalculatorPage(driver)
    
    try:
        # 1. Открытие страницы
        calculator.open()
        
        # 2. Установка задержки
        calculator.set_delay(45)
        
        # 3. Нажатие кнопок
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            calculator.click_button(button)
        
        # 4. Проверка, что результат НЕ появляется сразу
        start_time = time.time()
        assert calculator.is_result_not_present(), "Результат появился слишком быстро!"
        print("Результат не появился сразу (ожидаемо)")
        
        # 5. Ожидание результата
        calculator.get_result()
        
        # 6. Проверка времени выполнения
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Фактическое время выполнения: {execution_time:.2f} секунд")
        
        # Проверка что результат появился примерно через 45 секунд
        assert 43 <= execution_time <= 47, \
            f"Время выполнения {execution_time:.2f} сек не соответствует ожидаемому (45±2 сек)"
        
        print(f"Тест пройден успешно! Результат появился через {execution_time:.2f} секунд")

    except Exception as e:
        print(f"Ошибка во время выполнения теста: {str(e)}")
        driver.save_screenshot("lesson7_hw\error.png")
        raise    

    finally:
        driver.quit()

if __name__ == "__main__":
    print("Запуск теста...")
    test_slow_calculator()
    print("Тест завершен")

# pytest lesson7_hw\calc_test_run.py -s