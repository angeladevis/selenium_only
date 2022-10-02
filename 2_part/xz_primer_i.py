# запустить  просмотеть
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://yandex.ru/")

button = browser.find_element_by_css_selector('[data-id="images"]')
button.click()

browser.implicitly_wait(5)
browser.switch_to.window(browser.window_handles[1])
img = browser.find_element_by_css_selector(".PopularRequestList-Item_pos_0")
img.click()

browser.implicitly_wait(5)
img_1 = browser.find_element_by_css_selector(".serp-item__link")
img_1.click()

browser.implicitly_wait(5)
arrow_right = browser.find_element_by_xpath("/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]/i")
arrow_right.click()

browser.implicitly_wait(5)
arrow_left = browser.find_element_by_xpath("/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]/i")
arrow_left.click()


browser.quit()