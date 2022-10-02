'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 2, 6 степ (2_1_5) методом сокрытия футтера
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

# переход на нужную страницу
link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# функция, которая находит значение выражения при заданном x 
def calc(x):
	return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )

# находим значение x для выполнения задания
x_in_first_test = browser.find_element(By.ID, "input_value")
x_value = x_in_first_test.text

# высчитываем результат для первого задания
first_test_result = calc(x_value)

# вводим ответ к первому тесту
first_test_input = browser.find_element(By.ID, "answer")
first_test_input.send_keys(first_test_result)

#scroll \добавляем 2 строки к 2_1_5
# browser.execute_script("window.scrollBy(0, 100);") #Эта команда проскроллит страницу на 100 пикселей вниз
footer = browser.find_element(By.TAG_NAME, "footer")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) #2-й вариант, и эту дичь добавляем для скролла
browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer) #3-й вариант, скрываем футер

# выбираем checkbox
robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
robot_checkbox.click()

# выбираем radiobutton
robot_radiobutton = browser.find_element(By.ID, "robotsRule")
robot_radiobutton.click()

# нажимаем кнопку отправить
send_button = browser.find_element(By.CLASS_NAME, "btn-primary")
send_button.click()

time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
browser.quit()
