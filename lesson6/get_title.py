from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome.get("https://ya.ru")

# получаем в переменную название вкладки браузера
current_title = chrome.title

print(current_title)

chrome.quit()