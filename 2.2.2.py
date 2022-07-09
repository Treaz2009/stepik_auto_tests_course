from cmath import log
import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = math.log(abs(12 * math.sin(int(x))))
    browser.find_element_by_xpath('//*[@id="answer"]').send_keys(str(y))
    browser.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
    browser.execute_script("window.scrollTo(0, 99)")
    browser.find_element_by_css_selector("button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
