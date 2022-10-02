'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 3, 4 степ
'''

from selenium import webdriver
from selenium.webdriver.common.by import By 
import math, time

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

#
button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

#
confirm = browser.switch_to.alert
confirm.accept()

#
def calc(x):
    return( str( math.log( abs( 12 * math.sin( int(x))))))

#
x_element = browser.find_element(By.ID, 'input_value')
#
x_value = x_element.text

#
result = calc(x_value)

#
input = browser.find_element(By.ID, 'answer')
#
input.send_keys(result)

#
button2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button2.click()

time.sleep(5)

browser.quit()

