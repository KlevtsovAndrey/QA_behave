from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from behave import *

@given(u'Get to avtodispetcher "{url}"')
def step_impl(context, url):
    window_before = context.browser.window_handles[0]
    context.browser.find_element(By.ID, 'text').send_keys('расчет расстояний между городами')
    context.browser.find_element(By.XPATH, '//div[@class="search2__button"]').click()
    context.browser.implicitly_wait(5)
    context.browser.find_element(By.XPATH, '//a[starts-with(@href, "https://www.avtodispetcher.ru")]').click()

@when(u'We are on avtodispetcher')
def step_impl(context):
    window_after = context.browser.window_handles[1]
    context.browser.switch_to.window(window_after)
    assert context.browser.title == 'Расчет расстояний между городами'
    print('Произведен вход на сайт www.avtodispetcher.ru')
    context.browser.implicitly_wait(5)

@then(u'Enter initial route (г. Тула - г. Санкт-Петербург)')
def step_impl(context):
    context.browser.execute_script("window.scrollBy(0,500)", "")
    context.browser.find_element(By.NAME, 'from').send_keys('Тула')
    context.browser.find_element(By.NAME, 'to').send_keys('Санкт-Петербург')
    context.browser.find_element(By.NAME, 'fc').clear()
    context.browser.find_element(By.NAME, 'fc').send_keys('9')
    context.browser.find_element(By.NAME, 'fp').clear()
    context.browser.find_element(By.NAME, 'fp').send_keys('46')
    context.browser.find_element(By.XPATH, '//div[@class="submit_button"]//input').click()
    context.browser.implicitly_wait(5)
    print('Данные о маршруте "г. Тула - г. Санкт-Петербург": ')
    distance = context.browser.find_element(By.XPATH, '//span[@id="totalDistance"]')
    assert distance.text == '897'
    print('Расстояние:' + distance.text + 'км')
    EC.text_to_be_present_in_element((By.ID, 'f_fp'), '3726')
    print('Цена: 3726 руб.')

@then(u'Add a city to the route (г. Тула - г. Великий Новгород - г. Санкт-Петербург)')
def step_impl(context):
    context.browser.implicitly_wait(5)
    context.browser.execute_script("window.scrollBy(0,500)", "")
    context.browser.implicitly_wait(5)
    el = context.browser.find_element(By.ID, 'triggerFormD')
    hover = ActionChains(context.browser).move_to_element(el)
    hover.perform()
    el.click()
    context.browser.implicitly_wait(5)
    context.browser.find_element(By.NAME, 'v')
    context.browser.find_element(By.NAME, 'v').clear()
    context.browser.find_element(By.NAME, 'v').send_keys('Великий Новгород')
    print('В маршрут добавлен Великий Новгород')
    context.browser.implicitly_wait(60)
    subButton = context.browser.find_element(By.XPATH, '//div[@class="submit_button"]//input')
    context.browser.execute_script("arguments[0].scrollIntoView();", subButton)
    subButton.click()
    print('Данные о маршруте "г. Тула - г. Великий Новгород - г. Санкт-Петербург": ')
    distance2 = context.browser.find_element(By.XPATH, '//span[@id="totalDistance"]')
    assert distance2.text == '966'
    print('Новое расстояние: ' + distance2.text + 'км')
    EC.text_to_be_present_in_element((By.ID, 'f_fp'), '4002')
    print('Новая цена: 4002 руб.')
    print('Тест завершен успешно')
    print('Новая цена: 4002')

