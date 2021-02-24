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
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()