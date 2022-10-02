from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    url = 'http://suninjuly.github.io/registration2.html'
    browser.get(url)

    xpath = "//label[contains(text(), '*')]/following-sibling::input"
    input_list = browser.find_elements_by_xpath(xpath)
    output_list = ['first_name', 'Last_name', 'email']
    submit = browser.find_element_by_tag_name('button')

    for element, data in zip(input_list, output_list):
        element.send_keys(data)
    submit.click()

    time.sleep(5)

    welcome_text = browser.find_element_by_tag_name('h1').text
    assert 'Congratulations' in welcome_text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    