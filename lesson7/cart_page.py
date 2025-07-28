from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

  def __init__(self, browser):
    self._driver = browser

  def get(self):
    self._driver.get("https://www.labirint.ru/cart/")

  def get_counter(self):
    count = WebDriverWait(self._driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#basket-default-prod-count2"))
    ).text
        
    total_count = int(count.split(' ')[0])
    print(f"книг в корзине: {count}")
    return total_count
