from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# хз че это


try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(2)

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    static_message = "Verification was successful!"
   

    assert static_message == message.text, "Сообщение в алерте не то, что надо"
    
finally:
    time.sleep(2)
    browser.quit()