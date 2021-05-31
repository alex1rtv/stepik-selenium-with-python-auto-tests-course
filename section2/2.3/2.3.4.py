# https://stepik.org/lesson/184253/step/4?next=&unit=158843

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # check on first page
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)   

    # go to another page
    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    
    # now check on another page
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    # browser.execute_script("window.scrollBy(0, 100)")

    textbox = browser.find_element_by_css_selector("#answer")
    textbox.send_keys(y)    

    button = browser.find_element_by_tag_name("button")
    button.click()    
    
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    






























