from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

  def __init__(self, driver):
    self._driver = driver
    self._driver.get("https://www.labirint.ru/")
    self._driver.implicitly_wait(4)
    self._driver.maximize_window()

  def set_cookie_policy(self):
    cookie = {
      "name": "cookie_policy",
      "value": "1"
    }
    self._driver.add_cookie(cookie)
    print('меня вызвали')

  def search(self, term):
    # найти все книги по слову python
    search_field = WebDriverWait(self._driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#search-field"))
    )
    search_field.send_keys(term)
    self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()