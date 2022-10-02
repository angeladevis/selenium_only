from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
# button.click()

# button = browser.find_element_by_tag_name("button") тож самое по сути
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) #вот эту дичь добавляем для скролла
#false прокручивает вверх 
browser.execute_script("window.scrollBy(0, 100);") #Эта команда проскроллит страницу на 100 пикселей вниз:
button.click()

time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
browser.quit()

# // на javascript тож самое, через консоль можно проверить
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);
