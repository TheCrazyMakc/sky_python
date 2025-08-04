from selenium import webdriver
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
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

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
                         # переходим на страницу cart.html
                         .go_to_cart()
                         # переходим на checkout-step-one.html
                         .proceed_to_checkout()
                         # заполняем поля
                         .fill_info("Maxim", "Skypro", "123456")
                         # переходим на checkout-step-two.html
                         .continue_to_overview())

        # 4. Проверка суммы
        total_amount = checkout_page.get_total_amount()
        expected_amount = 58.29

        assert abs(total_amount - expected_amount) < 0.01, \
            f"Сумма не совпадает. Ожидалось: {expected_amount}, " \
            f"Получено: {total_amount}"

        print(f"Тест пройден успешно! Итоговая сумма: ${total_amount:.2f}")

    except Exception as e:
        print(f"Ошибка во время выполнения теста: {str(e)}")
        driver.save_screenshot("lesson7_hw\\error.png")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop_run()  # Выполнится ТОЛЬКО при запуске файла.
