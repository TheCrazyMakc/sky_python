from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:

  def __init__(self, browser):
    self._driver = browser

  def add_books(self):
     # ожидание загрузки результатов
    WebDriverWait(self._driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "._btn.btn-tocart.buy-link"))
    )
        
    # добавить все книги в корзину
    buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
        
    for btn in buy_buttons:
        try:
            btn.click()
            counter += 1
            sleep(1)  # Добавлена небольшая задержка между кликами
        except Exception as e:
            print(f"Не удалось кликнуть на кнопку: {e}")
    return counter