from msilib.schema import CheckBox, RadioButton
from tkinter import Radiobutton
from tkinter.ttk import Button
from selenium import webdriver
from cProfile import label
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)
  x_element = browser.find_element_by_xpath ("//img[@id='treasure'][1]")
  x_element = x_element.get_attribute ('valuex')
  x = x_element
  y = calc(x)
  Element=browser.find_elements_by_id("answer")
  for element in Element:
    element.send_keys(y) 

  CheckBox = browser.find_elements_by_xpath("//input[@id='robotCheckbox'][1]")
  input.type=("checkbox") 
  CheckBox.click()

  Radiobutton = browser.find_elements_by_xpath("//input[@id='robotsRule'][1]")
  RadioButton.click()

  Button = browser.find_element_by_css_selector ("button.btn")
  Button.click()
  
  time.sleep(10)      


finally:
 time.sleep(10)
 browser.quit()
