from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# зайти на сайт лабиринт
driver.get("https://www.labirint.ru")

# размер окна
driver.set_window_size(640, 480)

# найти книги по слову Python
search_input = driver.find_element(By.CSS_SELECTOR, '#search-field')
search_input.send_keys("Python", Keys.RETURN)

# Явное ожидание загрузки результатов
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-card"))
    )
except:
    print("Результаты поиска не загрузились")

# собрать все карточки товаров (лучше искать по более общему селектору)
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

for book in books:
    price = ""
    author = ""
    title = ""

    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
    except:
        author = 'Автор не указан' 
        
    try:
        title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    except:
        title = 'не указан' 

    try:
        price = book.find_element(By.CSS_SELECTOR, 'div.product-card[data-discount-price]').text
    except:
        price = 'не указан' 

    # print(author)
    # print(title)
    # print(price)
    print(author + '\t' + title + '\t' + price)

# Не забывайте закрывать драйвер
driver.quit()

# $$("div.product-card[data-discount-price]")
# $$('a.product-card__name')
