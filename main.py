import os
import random
from turtledemo.penrose import start
from selenium import webdriver
from time import perf_counter
import time
from bs4 import BeautifulSoup

def main():

    browser = webdriver.Chrome(executable_path='./chromedriver')
    link = 'https://thispersonnotexist.org'

    ans = req.get(link, proxies=None).text
    soup = BeautifulSoup(ans, 'lxml')

    # находим блок с картинками
    block = soup.find('div', class_='tabs')
    all_image = block.find_all('div', attrs={'xtpx': 'R'})

    print(block)
    for img in all_image:
        image_link = img.find('a').get('href')
        extension = image_link.headers['content-type'].split('/')[-1]
        filename = gener_filename(extension)

        with open(os.path.join('image', filename), 'wb') as file:
            file.write(ans.content)
        print(f'images: {1} finished..')

def gener_filename(file_extension):
    tmp = str(int(time.time()))
    for _ in range(5):
        tmp += chr(random.randint(65, 75))
    return f'{tmp}.{file_extension}'



if __name__ == '__main__':
    start = perf_counter()
    main()
    print(f'time: {(perf_counter() - start):.02f}')

