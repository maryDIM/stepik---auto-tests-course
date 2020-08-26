import pytest
from selenium import webdriver

import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"
                                  ])
def test_guest_should_see_answer(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_css_selector(".string-quiz__textarea")
    answer = str(math.log(int(time.time())))
    input1.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    # находим элемент, содержащий текст
    text_elt = browser.find_element_by_class_name("smart-hints__hint")
    # записываем в переменную text текст из элемента text_elt
    text = text_elt.text
    print(text)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Correct!" == text

    time.sleep(5)

