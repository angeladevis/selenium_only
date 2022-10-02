from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

#
def calc(x):
    return str( math.log( abs( 12*math.sin( x))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 15 секунд, пока цена не станет 100
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
            # EC.element_to_be_clickable((By.ID, "verify")) заменяем правило

    but_book = browser.find_element(By.ID, 'book')    
    but_book.click()

    # message = browser.find_element(By.ID, "verify_message")

    # assert "successful" in message.text
    # находим элемент
    x_element = browser.find_element(By.ID, 'input_value')
    # присваиваем текст между тегами переменной
    x_between_teg = x_element.text
    # значение между тегами пихаем в ф-ю
    x = calc(x_between_teg)
    # находим элемент 
    input = browser.find_element(By.NAME, name="text")
    # ответ ф-и вставляем в инпут
    input.send_keys(x)
    #
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
