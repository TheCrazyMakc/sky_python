from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

cookie = {
    "name": "cookie_policy",
    "value": "1"
}

browser = None

def open_labirint():
    # перейти на сайт Лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()  # Добавлены скобки для вызова метода
    browser.add_cookie(cookie)

def search(term):
    # найти все книги по слову python
    search_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#search-field"))
    )
    search_field.send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def add_books():
     # ожидание загрузки результатов
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "._btn.btn-tocart.buy-link"))
    )
        
    # добавить все книги в корзину
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
        
    for btn in buy_buttons:
        try:
            btn.click()
            counter += 1
            sleep(1)  # Добавлена небольшая задержка между кликами
        except Exception as e:
            print(f"Не удалось кликнуть на кнопку: {e}")
    return counter

    print(f"Добавлено книг в корзину: {counter}")
    sleep(3)

def go_to_cart():
    browser.get("https://www.labirint.ru/cart/")
    count = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#basket-default-prod-count2"))
    ).text
        
    total_count = int(count.split(' ')[0])
    print(f"книг в корзине: {count}")

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    open_labirint()
    search("python")
    add_books()
    added = add_books()
    go_to_cart()
    browser.quit()
        

if __name__ == "__main__":
    test_cart_counter()