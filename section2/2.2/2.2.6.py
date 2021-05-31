# https://stepik.org/lesson/228249/step/4?next=&unit=200781

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100)")

    textbox = browser.find_element_by_css_selector("#answer")
    textbox.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckBox")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()

    button = browser.find_element_by_tag_name("button")
    button.click()    
    
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    






























