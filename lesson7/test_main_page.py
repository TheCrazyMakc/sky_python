from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from main_page import MainPage
from result_page import ResultPage
from cart_page import CartPage

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('no book search term')

    result_page = ResultPage(browser)
    to_be = result_page.add_books()
    print(to_be)

    cart_page = CartPage(browser)
    cart_page.get()
    as_is = cart_page.get_counter()
    print(as_is)

    assert as_is == to_be
    sleep(5)
    browser.quit()

# def test_empty_search_result():
#     browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#     main_page = MainPage(browser)
#     main_page.set_cookie_policy()
#     main_page.search('no book search term')

# pytest lesson7\test_main_page.py -s