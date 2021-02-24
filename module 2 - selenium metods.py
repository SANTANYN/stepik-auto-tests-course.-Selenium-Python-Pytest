from selenium import webdriver
import time
import math
import unittest
#first task
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
check = browser.find_element_by_css_selector('#robotCheckbox')
check.click()
rabaton = browser.find_element_by_css_selector('#robotsRule')
rabaton.click()
sub = browser.find_element_by_css_selector('body > div.container > form > button')
sub.click()

#second task

#second task
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")
x_element = browser.find_element_by_css_selector('#treasure')
x = x_element.get_attribute("valuex")
y = calc(x)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
check = browser.find_element_by_css_selector('#robotCheckbox')
check.click()
rabaton = browser.find_element_by_css_selector('#robotsRule')
rabaton.click()
sub = browser.find_element_by_css_selector('body > div.container > form > div > div > button')
sub.click()
#third task

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


browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.execute_script("window.scrollBy(0, 100);")
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
#four task
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
browser.execute_script("window.scrollBy(0, 100);")
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(int(x))
browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector("#robotCheckbox").click()
browser.find_element_by_css_selector("#robotsRule").click()
browser.find_element_by_css_selector("body > div > form > button").click()

#five task

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
browser.find_element_by_css_selector("body > div.container > form > div > input:nth-child(2)").send_keys("dfdfddfdf")
browser.find_element_by_css_selector("body > div.container > form > div > input:nth-child(4)").send_keys("dfdfddfdf")
browser.find_element_by_css_selector("body > div.container > form > div > input:nth-child(6)").send_keys("dfdfddfdf")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'gggg.txt')           # добавляем к этому пути имя файла
browser.find_element_by_css_selector("#file").send_keys(file_path)
browser.find_element_by_css_selector(".btn").click()

#six task

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
browser.find_element_by_css_selector("body > form > div > div > button").click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)
browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector("body > form > div > div > button").click()

#seven task

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
browser.find_element_by_css_selector("body > form > div > div > button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)
browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector("body > form > div > div > button").click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element_by_id("book").click()
browser.execute_script("window.scrollBy(0, 500);")
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)
browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector("#solve").click()