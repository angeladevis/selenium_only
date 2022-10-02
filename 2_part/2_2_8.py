'''
Тут расположено решение тестового задания по курсу 
"Автоматизация тестирования с помощью Selenium и Python"
Модуль 2, раздел 2, степ 8
'''
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

# создаём объект браузера
browser = webdriver.Chrome()
browser.get(link)

# находим элемент и заполняем форму
first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
first_name.send_keys('Имя')

# находим элемент и заполняем форму
last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
last_name.send_keys('Фамилия')

# находим элемент и заполняем форму
email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
email.send_keys('aa@aa.aa')

# находим путь до текущей папки \ получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "test.txt"
# достраиваем его до пути до нужного файла \ добавляем к этому пути имя файла 
file_path = os.path.join(current_dir, file_name)
# находим нужный элемент на странице
element = browser.find_element(By.ID, "file")
# посылаем этот файл 
element.send_keys(file_path)

# находим элемент и кликаем
submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit.click()

#
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(__file__))


time.sleep(5)

browser.quit()