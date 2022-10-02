from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    # 1-й. аттрибут .text возвращает текст, который находится между открывающимся и закрывающимися тегами
    # проблема была в этом
    x = num1.text
    y = num2.text
    answer = str(int(x) + int(y))
    print(answer)
    # def sum(num1, num2):
    #     return str(num1 + num2)

    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    # browser.find_element(By.CSS_SELECTOR, "[value='answer']").click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer) # 2-й. ищем элемент с текстом "Python"
    button = browser.find_element_by_xpath("//button[(text()='Submit')]").click()# 3-й  важный момент

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()