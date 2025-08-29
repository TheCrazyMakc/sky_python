import allure
from selenium import webdriver
from shop_class import LoginPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Константы
TIMEOUT = 10
SHORT_TIMEOUT = 2
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@allure.feature("Интернет-магазин SauceDemo")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("""
Этот тест проверяет полный процесс оформления заказа:
1. Авторизация пользователя
2. Добавление товаров в корзину
3. Оформление заказа
4. Проверка итоговой суммы
""")
def test_shop_run():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    try:
        # 1. Логин
        with allure.step("Авторизация пользователя"):
            inventory_page = LoginPage(driver).open().login(USERNAME, PASSWORD)
            inventory_page.wait_for_load()
            allure.attach(f"Пользователь: {USERNAME}", name="Учетные данные")

        # 2. Добавление товаров
        with allure.step("Добавление товаров в корзину"):
            (inventory_page
             .add_item_to_cart("add-to-cart-sauce-labs-backpack")
             .add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
             .add_item_to_cart("add-to-cart-sauce-labs-onesie"))
            allure.attach("Добавлены товары: Рюкзак, Футболка, Комбинезон", 
                         name="Товары в корзине")

        # 3. Переход в корзину и оформление
        with allure.step("Оформление заказа"):
            checkout_page = (inventory_page
                             .go_to_cart()
                             .proceed_to_checkout()
                             .fill_info("Maxim", "Skypro", "123456")
                             .continue_to_overview())
            allure.attach("Информация о доставке: Maxim Skypro, 123456", 
                         name="Данные доставки")

        # 4. Проверка суммы
        with allure.step("Проверка итоговой суммы заказа"):
            total_amount = checkout_page.get_total_amount()
            expected_amount = 58.29
            
            allure.attach(f"Ожидаемая сумма: ${expected_amount:.2f}", 
                         name="Ожидаемая сумма")
            allure.attach(f"Фактическая сумма: ${total_amount:.2f}", 
                         name="Фактическая сумма")
            
            assert abs(total_amount - expected_amount) < 0.01, \
                f"Сумма не совпадает. Ожидалось: {expected_amount}, " \
                f"Получено: {total_amount}"

        with allure.step("Тест пройден успешно"):
            print(f"Тест пройден успешно! Итоговая сумма: ${total_amount:.2f}")
            allure.attach(f"Итоговая сумма: ${total_amount:.2f}", 
                         name="Результат теста")

    except Exception as e:
        with allure.step("Ошибка во время выполнения теста"):
            error_msg = f"Ошибка во время выполнения теста: {str(e)}"
            print(error_msg)
            driver.save_screenshot("lesson7_hw\\error.png")
            allure.attach.file("lesson7_hw\\error.png", name="Скриншот ошибки")
            allure.attach(error_msg, name="Текст ошибки")
            raise

    finally:
        with allure.step("Завершение работы драйвера"):
            driver.quit()


if __name__ == "__main__":
    test_shop_run()  # Выполнится ТОЛЬКО при запуске файла.