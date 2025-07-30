from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from shop_test_class import LoginPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# Константы
TIMEOUT = 10
SHORT_TIMEOUT = 2
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_shop_run():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # гугл хром выдает предупреждение, что пароль был раскрыт. Из-за этого не получается проверить тест в хроме.
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
        # 1. Логин
        inventory_page = LoginPage(driver).open().login(USERNAME, PASSWORD)
        inventory_page.wait_for_load()
        
        # 2. Добавление товаров
        (inventory_page
            .add_item_to_cart("add-to-cart-sauce-labs-backpack")
            .add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
            .add_item_to_cart("add-to-cart-sauce-labs-onesie"))
        
        # 3. Переход в корзину и оформление
        checkout_page = (inventory_page
            .go_to_cart() # переходим на страницу https://www.saucedemo.com/cart.html
            .proceed_to_checkout() # переходим на страницу https://www.saucedemo.com/checkout-step-one.html
            .fill_info("Maxim", "Skypro", "123456") # заполняем поля на странице
            .continue_to_overview()) # переходим на страницу https://www.saucedemo.com/checkout-step-two.html
        
        # 4. Проверка суммы
        # в переменную кладем результат функции
        total_amount = checkout_page.get_total_amount()
        # число, с которым должны будем проверить ответ
        expected_amount = 58.29

        # если условие True, assert не вызывает ошибку и код продолжает работу. иначе будет выполнено действие после \
        assert abs(total_amount - expected_amount) < 0.01, \
            f"Сумма не совпадает. Ожидалось: {expected_amount}, Получено: {total_amount}"
        
        print(f"Тест пройден успешно! Итоговая сумма: ${total_amount:.2f}")
    # обработчик исключений
    # Ловит любую ошибку, которая произошла в блоке try и cохраняет её в переменную e
    except Exception as e:
        print(f"Ошибка во время выполнения теста: {str(e)}")
        driver.save_screenshot("lesson7_hw\error.png")
        raise  
    finally:
        driver.quit()

if __name__ == "__main__":
    test_shop_run() # Выполнится ТОЛЬКО при запуске файла.

# pytest lesson7_hw\shop_test_run.py -s