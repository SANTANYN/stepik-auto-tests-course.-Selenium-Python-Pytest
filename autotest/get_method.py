import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
#driver.get("https://stepik.org/lesson/25969/step/12")
driver.get("http://suninjuly.github.io/cats.html")
time.sleep(2)
# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста .textarea
textarea = driver.find_element_by_class_name("el-input__inner")
time.sleep(2)
textarea.send_keys("mikhailtest")

# Напишем текст ответа в найденное поле  get()
#textarea.send_keys("mikhailtest")
#time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
#submit_button = driver.find_element_by_css_selector(".submit-submission")
submit_button = driver.find_element_by_css_selector(".submit-submission")
# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
