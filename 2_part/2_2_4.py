from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';")

browser.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
browser.quit()