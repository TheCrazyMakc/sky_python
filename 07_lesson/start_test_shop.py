from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from task2_shop import LoginPage


# Константы
TIMEOUT = 10
SHORT_TIMEOUT = 2
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_saucedemo_checkout():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
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
            .go_to_cart()
            .proceed_to_checkout()
            .fill_info("Maxim", "Skypro", "123456")
            .continue_to_overview())
        
        # 4. Проверка суммы
        total_amount = checkout_page.get_total_amount()
        expected_amount = 58.29

        assert abs(total_amount - expected_amount) < 0.01, \
            f"Сумма не совпадает. Ожидалось: {expected_amount}, Получено: {total_amount}"
        
        print(f"Тест пройден успешно! Итоговая сумма: ${total_amount:.2f}")

    except Exception as e:
        print(f"Ошибка во время выполнения теста: {str(e)}")
        driver.save_screenshot("error.png")
        raise  
    finally:
        driver.quit()

if __name__ == "__main__":
    test_saucedemo_checkout()