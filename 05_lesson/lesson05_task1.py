from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
  driver.get("http://uitestingplayground.com/classattr")

  search_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

  search_btn.click()

  sleep(10)

finally:
  driver.quit()