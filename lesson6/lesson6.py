from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def make_screenshot(browser):
    try:
        browser.maximize_window()
        browser.get("http://ya.ru")
        sleep(5)  # лучше заменить на WebDriverWait в реальном проекте
        browser.save_screenshot('./ya_'+browser.name+'.png')
    except Exception as e:
        print(f"Ошибка при работе с {browser.name}: {e}")
    finally:
        browser.quit()

# Создаем и работаем с каждым браузером по очереди
browser_ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
make_screenshot(browser_ff)

browser_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
make_screenshot(browser_chrome)

# browser_edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# make_screenshot(browser_edge)