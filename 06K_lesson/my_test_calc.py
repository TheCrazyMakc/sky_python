from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Инициализация драйвера Edge
# driver = webdriver.Edge(
#     service=EdgeService(EdgeChromiumDriverManager().install()))

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    buttons = ["7", "+", "8"]
    for button in buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()  
        
    result_element = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen"))).text
    
    print(result_element)

finally:
    driver.quit()