"""Automatically plays the game 2048."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path = 'D:\documents\leerplek\python\geckodriver-v0.26.0-win64\geckodriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')
html_elem = browser.find_element_by_tag_name('html')

while True:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
html_elem.send_keys(Keys.LEFT)
