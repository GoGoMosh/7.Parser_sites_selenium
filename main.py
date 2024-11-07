import os
import random
from turtledemo.penrose import start
from selenium import webdriver
from time import perf_counter
import time
from bs4 import BeautifulSoup

def main():

    # Т. к. веб-страница загружает картинки динамически, то придётся использовать selenium для обработки
    browser = webdriver.Firefox()
    browser.get('https://thispersonnotexist.org')
    time.sleep(15)


def gener_filename(file_extension):
    tmp = str(int(time.time()))
    for _ in range(5):
        tmp += chr(random.randint(65, 75))
    return f'{tmp}.{file_extension}'



if __name__ == '__main__':
    main()


