from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome.get("https://ya.ru")

# добавляем в переменную значение поиска на странице
element = chrome.find_element(By.CSS_SELECTOR, "#text")

# передаем в поисковую страницу текст
element.send_keys("test skypro")

# очищает текст из поля ввода
element.clear()

# в консоли найти кнопу "найти" на странице
# $$('button[type=submit]')
# находим и нажимаем кнопку 
chrome.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

sleep(5)

chrome.quit()