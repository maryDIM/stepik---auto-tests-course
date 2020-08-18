from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
#Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.


link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)

    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )

    #Нажать на кнопку "Book"
    button2 = browser.find_element_by_id("book")
    button2.click()

    # Решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button3 = browser.find_element_by_id("solve")
    button3.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла






