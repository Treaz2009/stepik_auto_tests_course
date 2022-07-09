from selenium import webdriver
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("ryu")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("tyu")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("fkk@hfj.ut")

    upload_button = browser.find_element_by_name("file")
# получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname('C:\Stepic.Homework\qwe'))
# добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'qwe.txt')
    upload_button.send_keys(file_path)

finally:
    button = browser.find_element_by_tag_name("button")
    button.click()
