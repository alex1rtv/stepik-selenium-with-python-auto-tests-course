# https://stepik.org/lesson/228249/step/8?next=&unit=200781

import os, time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # browser.execute_script("window.scrollBy(0, 100)")

    firstname = browser.find_element_by_css_selector("[name='firstname']")
    firstname.send_keys("Ivan")

    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("Petrov")

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("ivan.petrov@mail.ru")

    textname = "cv.txt"
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, textname)
    # добавляем к этому пути имя файла

    upload = browser.find_element_by_css_selector("[type='file']")
    upload.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()























