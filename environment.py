from selenium import webdriver
import os
import time
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    context.browser.delete_all_cookies()
    context.browser.get("http://yandex.ru")


def after_all(context):
    context.browser.quit()
