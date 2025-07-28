from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# Константы
TIMEOUT = 10
SHORT_TIMEOUT = 2
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.CSS_SELECTOR, "#user-name")
        self.password_field = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.driver.get(BASE_URL)
        return self

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return InventoryPage(self.driver)

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_list = (By.CSS_SELECTOR, ".inventory_list")
        self.shopping_cart = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def wait_for_load(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(self.inventory_list))
        return self

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
        self.first_name = (By.CSS_SELECTOR, "#first-name")
        self.last_name = (By.CSS_SELECTOR, "#last-name")
        self.postal_code = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.CSS_SELECTOR, "#continue")
        self.total_label = (By.CSS_SELECTOR, "div.summary_total_label")

    def fill_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_info")))
        
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        return self

    def continue_to_overview(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.continue_button)).click()
        return self

    def get_total_amount(self):
        total_element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.total_label))
        total_text = total_element.text
        return float(total_text.split('$')[1])

