from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# Константы
TIMEOUT = 10 # Максимальное время ожидания элементов (сек)
SHORT_TIMEOUT = 2 # Короткое время ожидания
BASE_URL = "https://www.saucedemo.com/" # URL тестируемого сайта
USERNAME = "standard_user" # Логин для авторизации
PASSWORD = "secret_sauce" # Пароль

class LoginPage:
    def __init__(self, driver):
        self.driver = driver # Передаём драйвер Selenium
        self.username_field = (By.CSS_SELECTOR, "#user-name") # Локатор поля логина (Это кортеж из двух элементов)
        self.password_field = (By.CSS_SELECTOR, "#password") # Локатор поля пароля
        self.login_button = (By.CSS_SELECTOR, "#login-button") # Локатор кнопки входа

    def open(self):
        self.driver.get(BASE_URL) # Открывает страницу в браузере
        return self # Возвращает сам объект, чтобы можно было делать цепочки вызовов

    def login(self, USERNAME, PASSWORD):
        # находим элемент по css селетору с ID:user-name и в это поле вписываем "standard_user"
        self.driver.find_element(*self.username_field).send_keys(USERNAME) # Звёздочка * распаковывает кортеж в отдельные аргументы
        self.driver.find_element(*self.password_field).send_keys(PASSWORD)
        # находим на странице кнопку по селектору и кликаем по ней
        self.driver.find_element(*self.login_button).click()
        return InventoryPage(self.driver) # Возвращает новую страницу (InventoryPage)

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_list = (By.CSS_SELECTOR, ".inventory_list") # добавляем локатор в переменную
        self.shopping_cart = (By.CSS_SELECTOR, "a.shopping_cart_link") # добавляем локатор в переменную

    # ждем пока загрузится часть страницы с карточками товара
    def wait_for_load(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(self.inventory_list)) # здесь * не нужна, потому что кортеж передается целиком
        return self
    
    # при вызове функции передаем в нее локатор нужной карточки (так как карточки 3шт будем вызывать функцию 3 раза, каждый раз с разным id)
    def add_item_to_cart(self, item_id):
        item_locator = (By.CSS_SELECTOR, f"#{item_id}")
        WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located(item_locator)).click()
        return self

    def go_to_cart(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.shopping_cart)).click()
        return CartPage(self.driver)

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.checkout_button)).click()
        return CheckoutPage(self.driver)

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.CSS_SELECTOR, "#first-name") # находим поля, которые будем заполнять
        self.last_name = (By.CSS_SELECTOR, "#last-name") # находим поля, которые будем заполнять
        self.postal_code = (By.CSS_SELECTOR, "#postal-code") # находим поля, которые будем заполнять
        self.continue_button = (By.CSS_SELECTOR, "#continue") # находим кнопку
        self.total_label = (By.CSS_SELECTOR, "div.summary_total_label") # находим нужный элемент с нужным нам текстом

    # находим элемент с полями для ввода
    def fill_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_info")))
        # заполняем поля
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        return self

    # нажимаем на кнопку
    def continue_to_overview(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.continue_button)).click()
        return self

    def get_total_amount(self):
        # добавляем найденный элемент в переменную
        total_element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.total_label))
        # получаем текст в переменную
        total_text = total_element.text
        # выводим только цифры, после символа $
        return float(total_text.split('$')[1])