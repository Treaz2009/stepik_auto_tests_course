from multiprocessing import Value
from pydoc import text
from select import select
from tkinter import Y
from selenium import webdriver
from cProfile import label
import math
import time
from selenium.webdriver.support.ui import Select


def sum(x, y):
    return str(sum(int[x]+int[y]))


try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_xpath('//*[@id="num1"]').text
    y = browser.find_element_by_xpath('//*[@id="num2"]').text
    sum = (int(x)+int(y))
    browser.find_element_by_xpath('//*[@id="dropdown"]').click()
    select = Select(browser.find_element_by_tag_name("select"))
    browser.find_element_by_css_selector(
        f'option[value="{int(x)+int(y)}"]').click()
    select = select(browser.find_element_by_css_selector(
        f'option[value="{int(x)+int(y)}"]'))

    browser.find_element_by_css_selector("button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
