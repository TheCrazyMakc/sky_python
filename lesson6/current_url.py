from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome.get("https://ya.ru")

# получаем в переменную ссылку сайта
url = chrome.current_url

print(url)

chrome.quit()