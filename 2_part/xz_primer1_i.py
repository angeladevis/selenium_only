# запустть просмотреть
from selenium import webdriver
import unittest
import time
 
 
class YandexImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.get('https://yandex.ru/')
 
    def test_01(self):
        driver = self.driver
        driver.find_element_by_link_text('Картинки').click()
        driver.switch_to.window(driver.window_handles[1])
 
        images = driver.find_elements_by_class_name('cl-teaser__link')
        images[0].click()
        time.sleep(3)
 
        driver.find_element_by_css_selector('.cl-viewer-navigate__item_right').click()
        time.sleep(5)
 
    def tearDown(self) -> None:
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()