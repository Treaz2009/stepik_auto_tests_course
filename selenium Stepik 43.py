from cProfile import label
from selenium import webdriver
import math 
import time

link = "http://suninjuly.github.io/find_link_text_redirect13.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("andei")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Samoilov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("becici")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Montenegro")
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла