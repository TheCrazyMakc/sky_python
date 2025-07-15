from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try: 
  driver.get("http://the-internet.herokuapp.com/inputs")

  search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

  search_input.send_keys("Sky")

  search_input.clear()

  search_input.send_keys("Pro")

  sleep(15)

finally:
  driver.quit()