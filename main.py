import os
import random
from turtledemo.penrose import start
from selenium import webdriver
from time import perf_counter
import time

def main():

    browser = webdriver.Firefox()
    browser.get('https://www.youtube.com')

    button = browser.find_element( 'xpath' , 'style-scope ytd-rich-grid-renderer')
    print(button)
    """
    # Т. к. веб-страница загружает картинки динамически, то придётся использовать selenium для обработки
    browser = webdriver.Firefox() # С FireFox легче работает, потому что сильно гибок в настройках
    browser.get('https://thispersonnotexist.org')
    time.sleep(5)
    browser.get('https://google.com')
    browser.save_screenshot('1.png')
    browser.refresh()
    browser.quit()
    """

if __name__ == '__main__':
    main()


