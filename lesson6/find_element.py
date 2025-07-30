from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome.get("https://www.labirint.ru/")

# находим элемент по селектору и берем из него текст
txt = chrome.find_element(By.CSS_SELECTOR, 'a.js-shelves-title').text
print(txt)

# берез значения стилей CSS
ff = chrome.find_element(By.CSS_SELECTOR, 'a.js-shelves-title').value_of_css_property("font-family")
print(ff)
sleep(5)

chrome.quit()