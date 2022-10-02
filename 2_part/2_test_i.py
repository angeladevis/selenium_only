from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://yandex.ru")
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()


