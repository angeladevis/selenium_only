from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://SunInJuly.github.io/execute_script.html")

try:
    button = driver.find_element(By.TAG_NAME, "button")
    _ = button.location_once_scrolled_into_view
    time.sleep(5)
    button.click()
    time.sleep(5)
    assert True #дзенбуддистский_котъ

finally:
    driver.quit()