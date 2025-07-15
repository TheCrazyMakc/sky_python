from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try: 
  driver.get("http://the-internet.herokuapp.com/login")

  search_input_login = driver.find_element(By.CSS_SELECTOR, '#username')

  search_input_login.send_keys("tomsmith")

  search_input_password = driver.find_element(By.CSS_SELECTOR, '#password')

  search_input_password.send_keys("SuperSecretPassword!")

  search_button_login = driver.find_element(By.CSS_SELECTOR, 'button.radius')

  search_button_login.click()

  div_text = driver.find_element(By.CSS_SELECTOR, 'div.flash.success').text

  print("Текст из div:", div_text)

  sleep(10)

finally:
  driver.quit()