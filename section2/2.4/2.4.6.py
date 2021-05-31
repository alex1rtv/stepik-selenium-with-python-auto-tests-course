# https://stepik.org/lesson/181384/step/6

from selenium import webdriver
import time

browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

# time.sleep(1)
button = browser.find_element_by_id("button")
button.click()

# message = browser.find_element_by_id("verify_message")
# assert "successful" in message.text

time.sleep(10)

browser.quit()
