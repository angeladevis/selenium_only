# ниче не понятно
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

#
time.sleep(2)

button = browser.find_element(By.ID, "verify")
button.click()
# message = browser.find_element(By.ID, "verify_message")

if browser.find_element(By.ID, 'verify_message').text == "Проверка прошла успешно, нихуа не понятно!":
    browser.close()
# assert "successful" in message.text
