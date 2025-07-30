from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# ЭТОТ КОД НЕ ХОЧЕТ РАБОТАТЬ
# chrome.get("https://uitestingplayground.com/visibility")
# is_displayed = chrome.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# print(is_displayed)

# chrome.find_element(By.CSS_SELECTOR, '#hideButton').click()
# sleep(2)

# is_displayed = chrome.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# print(is_displayed)
# sleep(2)


# проверка радио-кнопок
# chrome.get("https://demoqa.com/radio-button")

# is_enable = chrome.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
# print(is_enable)

# is_enable = chrome.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
# print(is_enable)


# проверка нажатия на чек-бокс
# chrome.get("https://the-internet.herokuapp.com/checkboxes")

# cb = chrome.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')

# is_selected = cb.is_selected()
# print(is_selected)

# cb.click()

# is_selected = cb.is_selected()
# print(is_selected)
# sleep(2)

chrome.get("https://the-internet.herokuapp.com/checkboxes")

div = chrome.find_element(By.CSS_SELECTOR, 'div.large-4')

a = chrome.find_element(By.CSS_SELECTOR, 'a')

print(a.get_attribute("href"))

chrome.quit()