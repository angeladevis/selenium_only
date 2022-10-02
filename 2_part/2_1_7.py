from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # x_element = browser.find_element(By.ID, "input_value")
    x_element = browser.find_element(By.TAG_NAME, 'img')
    # x_element = browser.find_element_by_css_selector('[valuex]')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    # print(y)
    input1 = browser.find_element(By.ID, "answer")
    # input1 = y \не так, а вот как надо было
    input1.send_keys(y) #былин, так просто

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    radiobutton1 = browser.find_element(By.ID, "robotsRule") # поменялся селектор
    radiobutton1.click()

    button1 = browser.find_element(By.XPATH, "//button[(text()='Submit')]")
    button1.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    