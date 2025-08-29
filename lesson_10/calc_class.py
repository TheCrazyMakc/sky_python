from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalcMainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.url)
        return self

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param seconds: int — время задержки в секундах.
        """
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")
            )
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    @allure.step("Нажатие кнопки '{button_text}'")
    def click_button(self, button_text):
        """
        Нажимает на кнопки калькулятора.

        :param button_text: str — текст на кнопке, которую нужно нажать.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']")
            )
        )
        button.click()
        return self

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self, timeout=50):
        """
        Возвращает текущий результат с экрана калькулятора.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
