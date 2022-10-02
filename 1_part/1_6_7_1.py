from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    letters = string.ascii_lowercase 
    # Создаем строку из букв англ. алфавита в нижнем регистре
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for field in elements:
        random_word = ''.join(random.choice(letters) for _ in range(8))
        #  В цикл добавляем генерацию случайного набора символов (диапазон произвольный)
        field.send_keys(random_word)
        #  И заполняем наше поле этим словом
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла 21.227605347283152
