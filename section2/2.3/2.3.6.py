# https://stepik.org/lesson/184253/step/6?next=&unit=158843

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # check on first page
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)   

    button = browser.find_element_by_tag_name("button")
    button.click()

    # go to another tab
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    
    # now check on another page
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

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

    






























