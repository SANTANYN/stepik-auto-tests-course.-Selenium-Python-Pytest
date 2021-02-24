import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import random
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
driver.get("https://kit-eu.voximplant.com/login")
driver.implicitly_wait(10)
import os
'''textarea = driver.find_element_by_class_name("el-input__inner")

textarea.send_keys("mikhailtest")

textarea = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div[1]/div[1]/input")

textarea.send_keys("msorokin@voximplant.com")

textarea = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div[1]/div[1]/input")

textarea.send_keys("Ms0665117437")
# Вход в кит
submit_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/button")
submit_button.click()
time.sleep(5)


# ТЕСТ - Создание api-tokena
# переход в интеграцию
submit_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/aside/nav/div[2]/div/div[1]/div/ul/a[7]")
submit_button.click()
time.sleep(5)
submit_button = driver.find_element_by_xpath("/html/body/div[1]/main/section/div[1]/ul/a[5]")
submit_button.click()
time.sleep(5)
submit_button = driver.find_element_by_xpath("/html/body/div[1]/main/section/section/div[2]/div/button")
submit_button.click()
time.sleep(5)
textarea = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/input")

textarea.send_keys(print("a"))
time.sleep(2)
submit_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/button[1]")
submit_button.click()
'''
#   ТЕСТ: Звонок черрез софтфон. Нужно придумат ькак решить проблемс с разрешением браузера.
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
'''driver.get("https://kit-eu.voximplant.com/login")
# Ищем поле для ввода текста .textarea
textarea = driver.find_element_by_class_name("el-input__inner")
# textarea.send_keys - пишем текст в инпут найденный с помощью find_element
textarea.send_keys("mikhailtest")
textarea = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div[1]/div[1]/input")
textarea.send_keys("msorokin@voximplant.com")
textarea = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div[1]/div[1]/input")
textarea.send_keys("Ms0665117437")
# Находим кнопку
submit_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/button")
# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
submit_button = driver.find_element_by_css_selector("#application > div.sidebars-wrap > div.soft-phone__wrapper > button")
submit_button.click()
submit_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/div[2]/button[2]")
submit_button.click()
textarea = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/input")
time.sleep(2)
textarea.send_keys("+79957953303")
time.sleep(2)
alert = driver.switch_to.alert
alert.text(["использование микрофона"])
alert.accept()
submit_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/div[3]/div[2]")
submit_button.click()
driver.quit()'''
'''''
# ТЕСТ -  Отправка сообщения.

driver.get("https://kit-eu.voximplant.com/login")
# Ищем поле для ввода текста .textarea
textarea = driver.find_element_by_class_name("el-input__inner")
# textarea.send_keys - пишем текст в инпут найденный с помощью find_element
textarea.send_keys("mikhailtest")
textarea = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div[1]/div[1]/input")
textarea.send_keys("msorokin@voximplant.com")
textarea = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div[1]/div[1]/input")
textarea.send_keys("Ms0665117437")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/form/button").click()
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/aside/nav/div[2]/div/div[2]/div[2]/ul/a[3]/div[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[1]/main/div[2]/div[2]/div/div[2]/div/div/p").send_keys("!/@#$%^&*()_+1qdDS?><}{|    sW}?||||_")
driver.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[2]/button").click()
assert driver.find_element_by_class_name("chat-datepicker__date") '''''