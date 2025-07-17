from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://www.uitestingplayground.com/progressbar")
    
    # Запуск прогресс-бара
    driver.find_element(By.CSS_SELECTOR, "#startButton").click()
    
    # Более точное отслеживание прогресса
    while True:
        progress_text = driver.find_element(By.CSS_SELECTOR, "#progressBar").text
        progress = int(progress_text.replace('%', ''))
        
        if progress >= 75:
            driver.find_element(By.CSS_SELECTOR, "#stopButton").click()
            break
        
        # Небольшая пауза для уменьшения нагрузки
        driver.implicitly_wait(0.05)
    
    print(driver.find_element(By.CSS_SELECTOR, "#result").text)

finally:
    driver.quit()