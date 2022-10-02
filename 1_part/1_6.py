# 1) импорт вебдрайвер
# 2) инициализация драйвера Хрома
# 3) открыть ссылку
# 4) найти кнопку по селектору
# 5) напечатать текст с кнопки
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
# найти элемент по id на указанной странице
print(button.text)
