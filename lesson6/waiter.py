from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#переход на страницу:
driver.get("http://www.uitestingplayground.com/progressbar")

#запуск индикатора прогресса:
driver.find_element(By.CSS_SELECTOR, "#startButton").click()

#затем подготовка драйвера к ожиданию:
waiter = WebDriverWait(driver, 40, 0.1) 

#ожидание выполнения условий:
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%")
)

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print(driver.find_element(By.CSS_SELECTOR, "#result").text)