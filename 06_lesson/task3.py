# ЗАДАНИЕ  3) Дождаться картинки

# Напишите скрипт.

# Шаги:
#     Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
#     Дождитесь загрузки всех картинок.
#     Получите значение атрибута src у 3-й картинки.
#     Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# Устанавливаем неявное ожидание
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

take_href = driver.find_element(By.CSS_SELECTOR, "#award")
src_value = take_href.get_attribute("src")
print(f"Значение атрибута src: {src_value}")

driver.quit()