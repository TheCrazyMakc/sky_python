from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# прописываем куки вручную
my_cookie = {
  'name': 'cookie_policy',
  'value': '1'
}

chrome.get("https://labirint.ru")

# добавляем куки на страницу
chrome.add_cookie(my_cookie)
chrome.refresh()

# получаем значение из куки
cookie = chrome.get_cookie('PHPSESSID')
print(cookie)

# получаем все куки
# cookies = chrome.get_cookies()
# print(cookies)

# удаляем куки
# chrome.delete_all_cookies()
# chrome.refresh()

# sleep(5)

chrome.quit()