'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 3, 4 степ
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

# находим элемент соответствующий плавающей кнопке и кликаем на нее
button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

#
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

#
def calc(x):
    return str ( math.log( abs( 12 * math.sin( int( x)))))

# находим элемент с значением х
x_element = browser.find_element(By.ID, 'input_value')
# присваиваем значение находящееся между тегами переменной
x_value = x_element.text
# подставляем значение х в функцию и сообщаем ответ в переменную
result = calc(x_value)

# находим элемент соответствующий полю ввода
input = browser.find_element(By.ID, 'answer')
# подставляем найденное ранее значение ф-и в поле ввода
input.send_keys(result)

# находим элемент соответствующий кнопке и кликаем на неё
button2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button2.click()

#
time.sleep(7)

#
browser.quit()






