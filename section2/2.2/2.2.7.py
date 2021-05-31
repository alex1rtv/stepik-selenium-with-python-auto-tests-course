# https://stepik.org/lesson/228249/step/7?next=&unit=200781

import os
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

browser.execute_script("window.scrollBy(0, 100)")

textbox = browser.find_element_by_css_selector("#answer")
# textbox.send_keys(y)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
textbox.send_keys(file_path)

print(os.path.abspath(__file__))
print("------------------------------------")
print(os.path.abspath(os.path.dirname(__file__)))






























