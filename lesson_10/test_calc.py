import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from calc_class import CalculatorPage


@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест медленного калькулятора с задержкой 45 секунд")
@allure.description("""
Этот тест проверяет работу калькулятора с установленной задержкой.
Ожидается, что результат операции появится через примерно 45 секунд.
""")
def test_slow_calculator():
    """
    Тест для проверки калькулятора с медленным вычислением.
    """
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    calculator = CalculatorPage(driver)

    try:
        # 1. Открытие страницы
        with allure.step("Открытие страницы калькулятора"):
            calculator.open()

        # 2. Установка задержки
        with allure.step("Установка задержки вычислений"):
            calculator.set_delay(2)

        # 3. Нажатие кнопок
        with allure.step("Выполнение вычисления 7 + 8"):
            buttons = ["7", "+", "8", "="]
            for button in buttons:
                calculator.click_button(button)
                allure.attach(f"Нажата кнопка: {button}", name="Действие")

        # 4. Проверка, что результат НЕ появляется сразу
        start_time = time.time()

        # 5. Ожидание результата
        with allure.step("Ожидание результата вычисления"):
            result = calculator.get_result()
            allure.attach(f"Полученный результат: {result}", name="Результат")

        # 6. Проверка времени выполнения
        with allure.step("Проверка времени выполнения"):
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Фактическое время выполнения: {execution_time:.2f} секунд")
            
            allure.attach(
                f"Фактическое время выполнения: {execution_time:.2f} секунд",
                name="Время выполнения"
            )

        # Проверка что результат появился примерно через 45 секунд
        with allure.step("Проверка соответствия времени выполнения"):
            assert 1 <= execution_time <= 5, \
                f"Время выполнения {execution_time:.2f} сек не соответствует " \
                f"ожидаемому (45±2 сек)"

        with allure.step("Тест пройден успешно"):
            print("Тест пройден успешно! "
                  f"Результат появился через {execution_time:.2f} секунд")
            allure.attach(
                f"Тест пройден! Время: {execution_time:.2f} сек",
                name="Статус теста"
            )

    except Exception as e:
        with allure.step("Ошибка во время выполнения теста"):
            print(f"Ошибка во время выполнения теста: {str(e)}")
            driver.save_screenshot("lesson7_hw\\error.png")
            allure.attach.file("lesson7_hw\\error.png", name="Скриншот ошибки")
            allure.attach(f"Ошибка: {str(e)}", name="Текст ошибки")
            raise

    finally:
        with allure.step("Завершение работы драйвера"):
            driver.quit()


if __name__ == "__main__":
    print("Запуск теста...")
    test_slow_calculator()
    print("Тест завершен")