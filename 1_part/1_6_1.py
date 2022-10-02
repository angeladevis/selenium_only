from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://yandex.ru") # загрузка здесь
button = browser.find_element(By.CLASS_NAME, "button" )