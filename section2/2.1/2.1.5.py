# https://stepik.org/lesson/165493/step/5?next=&unit=140087

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    textbox = browser.find_element_by_css_selector("#answer")
    textbox.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    






























