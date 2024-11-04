import os
import random
from turtledemo.penrose import start
from selenium import webdriver
from time import perf_counter
import time
from bs4 import BeautifulSoup

def main():

    # Т. к. веб-страница загружает картинки динамически, то придётся использовать selenium
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    service = webdriver.chrome.service.Service(executable_path=binary_yandex_driver_file)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://thispersonnotexist.org')
    driver.quit()


def gener_filename(file_extension):
    tmp = str(int(time.time()))
    for _ in range(5):
        tmp += chr(random.randint(65, 75))
    return f'{tmp}.{file_extension}'



if __name__ == '__main__':
    main()


