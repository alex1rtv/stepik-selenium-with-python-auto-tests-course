# https://stepik.org/lesson/165493/step/7?next=&unit=140087

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    img = browser.find_element_by_css_selector("img#treasure")
    x = img.get_attribute("valuex")
    y = calc(x)

    textbox = browser.find_element_by_css_selector("#answer")
    textbox.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("input[value='robots']")
    radiobutton.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    






























