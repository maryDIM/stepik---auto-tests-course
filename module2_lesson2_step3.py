from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = int(browser.find_element_by_id("num1").text)
    b = int(browser.find_element_by_id("num2").text)
    y = a+b

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


