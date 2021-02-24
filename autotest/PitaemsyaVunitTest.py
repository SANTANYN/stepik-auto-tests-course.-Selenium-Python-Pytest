import unittest
from selenium import webdriver
import time
import math

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("ok")


if __name__ == '__main__':
    unittest.main()


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
x_element = browser.find_element_by_css_selector('#num1')

y_element = browser.find_element_by_css_selector('#num2')


y = y_element.text
x = x_element.text
z = (int(x)+int(y))
# Тыкаем на селект по тегу чтобы он открылся
browser.find_element_by_css_selector("#dropdown").click()
#выбираем элемент селекта.
browser.find_element_by_css_selector("[value='" + str(z) + "']").click()
time.sleep(2)
rabaton = browser.find_element_by_css_selector('body > div.container > form > button')
rabaton.click()
