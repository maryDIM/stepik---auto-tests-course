
# напишем два теста: один из них будет проходить, а другой — нет. Посмотрим, как выглядит перезапуск.
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

#Мы увидим сообщение: "1 failed, 1 passed, 1 rerun in 9.20s﻿", то есть упавший тест был перезапущен,
#но при втором запуске тоже упал. Если бы во второй раз мигающий тест все-таки прошёл успешно,
# то мы бы увидели сообщение: ﻿﻿"2 passed, 1 rerun in 9.20s"﻿, и итоговый результат запуска всех тестов считался бы успешным.
