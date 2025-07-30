# для искусственных пауз между действиями
from time import sleep

# Управления браузером через Selenium WebDriver
from selenium import webdriver

# для Поиска элементов по разным локаторам: By.ID, By.CSS_SELECTOR, By.XPATH и т.д.
from selenium.webdriver.common.by import By

# для Автоматической настройки и управления драйвером Edge в Selenium
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# для Умного ожидания элементов (без sleep).
from selenium.webdriver.support.ui import WebDriverWait

# нужно для Готовых условий ожидания (видимость, кликабельность и др.).
# EC.visibility_of_element_located((By.ID, "element"))  # Ждёт, пока элемент станет видимым
from selenium.webdriver.support import expected_conditions as EC

# firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Chrome
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# FireFox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Инициализация драйвера Edge
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

try:
    driver.get("https://www.saucedemo.com/")

    # находим элемент по css селетору с ID:user-name и в это поле вписываем "standard_user"
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    # находим на странице кнопку по селектору и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    # Ждёт до 2 секунд, пока не найдёт кнопку добавления в корзину (#add-to-cart-sauce-labs-backpack) и сразу кликает на неё.
    # WebDriverWait(driver, 2) — ждёт максимум 2 секунды.
    # EC.presence_of_element_located — проверяет наличие элемента в DOM.
    # .click() — клик по найденной кнопке.
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()
    
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))).click()
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))).click()
    
    # Ждёт до 2 секунд, пока не найдёт поле ввода и вводит "Maxim"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name"))).send_keys("Maxim")
    
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Skypro")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))).click()
    
    # Проверка суммы
    total_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label"))).text
    
    # Извлечение числового значения из строки "Total: $58.29"
    # 1. split('$') разделяет строку по знаку доллара:
    #    → ["Total: ", "58.29"]
    # 2. [1] берёт второй элемент списка (индекс 1): 
    #    → "58.29"
    # 3. float() преобразует строку "58.29" в число 58.29
    total_amount = float(total_text.split('$')[1])
    expected_amount = 58.29

    # Проверка через assert
    # Вычисляет абсолютную разницу между числами
    # Если условие ложно → выводится сообщение об ошибке:
    assert abs(total_amount - expected_amount) < 0.01, \
        f"Сумма не совпадает. Ожидалось: {expected_amount}, Получено: {total_amount}"
    # :.2f — это форматирование числа с плавающей запятой (float):
    print(f"Тест пройден успешно! Итоговая сумма: ${total_amount:.2f}")

    # Пауза 2 секунды (не рекомендуется для production)
    sleep(2)

# Ловит любое исключение (ошибку) и сохраняет его в переменную e
except Exception as e:
    print(f"Ошибка во время выполнения теста: {str(e)}")
    # сохранит скриншот страницы в момент ошибки (удобно для отладки).
    driver.save_screenshot("error.png")
    # Повторно выбрасывает пойманное исключение, чтобы: Прервать выполнение, если это критическая ошибка.
    raise  

finally:
    driver.quit()