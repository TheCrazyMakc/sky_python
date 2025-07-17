from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome.get("https://ya.ru")

# меняем размер окна браузера
chrome.maximize_window()
chrome.minimize_window()
chrome.fullscreen_window()
chrome.set_window_size(1000, 600)

chrome.quit()