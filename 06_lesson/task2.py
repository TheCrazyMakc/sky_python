# ЗАДАНИЕ  2) Переименовать кнопку

# Напишите скрипт.

# Шаги:
#     Перейдите на сайт http://uitestingplayground.com/textinput.
#     Укажите в поле ввода текст SkyPro.
#     Нажмите на синюю кнопку.
#     Получите текст кнопки и выведите в консоль ("SkyPro")
# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# Устанавливаем неявное ожидание
driver.implicitly_wait(5)

driver.get("http://uitestingplayground.com/textinput")

text_form = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
text_form.clear() # Очищаем поле, если там есть текст
text_form.send_keys("SkyPro")

push_the_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
push_the_button.click()

# ЯВНОЕ ожидание
waiter = WebDriverWait(driver, 10) 

#ожидание выполнения условий:
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

# выводим текст кнопки
button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(button_text.text)

# sleep(3)

driver.quit()