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

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Инициализация драйвера Edge
# driver = webdriver.Edge(
#     service=EdgeService(EdgeChromiumDriverManager().install()))

try:
    driver.get("https://www.saucedemo.com/")

    input_login = driver.find_element(By.CSS_SELECTOR, "#user-name")
    input_login.send_keys("standard_user")

    input_password = driver.find_element(By.CSS_SELECTOR, "#password")
    input_password.send_keys("secret_sauce")

    # Нажатие кнопки Login
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    add_cart1 = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()
    
    add_cart2 = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    
    add_cart3 = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))).click()
    
    # inside_corzina = WebDriverWait(driver, 2).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "a.shopping_cart_link"))).click()
    
    # inside_checkout = WebDriverWait(driver, 2).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))).click()
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))).click()
    
    # input_first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    # input_first_name.send_keys("Maxim")

    # input_last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    # input_last_name.send_keys("Skypro")

    # input_zip_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    # input_zip_code.send_keys("123456")   

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name"))).send_keys("Maxim")
    
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Skypro")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")

    # push_continue = WebDriverWait(driver, 2).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#continue"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))).click()
    
    # total_cost = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

    # print(total_cost)

    # check_summ = 58.29

    # if int(float(total_cost)) == check_summ:
    #     print('Тест пройден, сумма = ' + check_summ)
    # else:
    #     print('Сумма не равна ' + check_summ)

    # Проверка суммы
    total_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label"))).text
    
    # Извлечение числового значения из строки "Total: $58.29"
    total_amount = float(total_text.split('$')[1])
    expected_amount = 58.29

    # Проверка через assert
    assert abs(total_amount - expected_amount) < 0.01, \
        f"Сумма не совпадает. Ожидалось: {expected_amount}, Получено: {total_amount}"
    
    print(f"Тест пройден успешно! Итоговая сумма: ${total_amount:.2f}")

except Exception as e:
    print(f"Ошибка во время выполнения теста: {str(e)}")
    # driver.save_screenshot("error.png")
    raise  


finally:
    driver.quit()
