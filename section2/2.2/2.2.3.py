# https://stepik.org/lesson/228249/step/3?unit=200781

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def total(x, y):
  return str(x + y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = int(browser.find_element_by_css_selector("#num1").text)
    y = int(browser.find_element_by_css_selector("#num2").text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(total(x, y))    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    






























