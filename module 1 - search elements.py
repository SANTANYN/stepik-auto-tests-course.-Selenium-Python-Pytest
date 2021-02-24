from selenium import webdriver
import time
import math

''' #first task
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    input1 = browser.find_element_by_css_selector("body > div.container > form > div:nth-child(1) > input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("body > div.container > form > div:nth-child(2) > input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("body > div.container > form > div:nth-child(3) > input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("#country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("#submit_button")
    button.click()
'''

'''''# Second task
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()
input1 = browser.find_element_by_css_selector("body > div.container > form > div:nth-child(1) > input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("body > div.container > form > div:nth-child(2) > input")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("body > div.container > form > div:nth-child(3) > input")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_css_selector("#country")
input4.send_keys("Russia")
button = browser.find_element_by_xpath("/html/body/div/form/button")
button.click()
'''''
'''#Third task
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
        element.send_keys("Йоба")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
'''
'''#fourth task
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
        element.send_keys("Йоба")
    button = browser.find_element_by_xpath("/html/body/div[1]//div[6]/button[3]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
#fifth task
'''
'''
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")
textarea = browser.find_element_by_css_selector('input.form-control.first')
textarea.send_keys("mikhail")
textarea = browser.find_element_by_css_selector('input.form-control.third')
textarea.send_keys("blablab333@mail.ru")
textarea = browser.find_element_by_css_selector('[class="form-control first"]')
textarea.send_keys("mikhail")
textarea = browser.find_element_by_css_selector('[class="form-control second"]')
textarea.send_keys("blablab333@mail.ru")
''' '''
button = browser.find_element_by_xpath("/html/body/div[1]/form/button")
button.click()
'''
'''
time.sleep(10)
browser.quit()
'''
'''#first
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    textarea = browser.find_element_by_css_selector('input:required.form-control.first')
    textarea.send_keys("mikhail")
    textarea = browser.find_element_by_css_selector('input:required.form-control.second')
    textarea.send_keys("input.form-control.second")
    textarea = browser.find_element_by_css_selector('input:required.form-control.third')
    textarea.send_keys("blablab333@mail.ru")
    textarea = browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[1]/input')
    textarea.send_keys("bwebe")
    textarea = browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[2]/input')
    textarea.send_keys("123")
    time.sleep(3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(3)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    '''
