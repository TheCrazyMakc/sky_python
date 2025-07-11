from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://ya.ru")

# # driver.save_screenshot('./lesson5/ya.png')

# driver.set_window_size(640, 480)

# sleep(10)

driver.get("https://www.labirint.ru")

driver.set_window_size(640, 480)

search_input = driver.find_element(By.CSS_SELECTOR, '#search-field')

search_input.send_keys("Python", Keys.RETURN)

books = driver.find_elements(By.CSS_SELECTOR, "div.product-card__price-current")

print(len(books))