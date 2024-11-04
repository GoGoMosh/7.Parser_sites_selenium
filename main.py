import os
import random
from turtledemo.penrose import start
import requests as req
from time import perf_counter
import time

def main():

    link = 'https://thispersonnotexist.org/downloadimage/Ac3RhdGljL21hbi9zZWVkMjE4MjEuanBlZw=='
    proxy = "185.21.60.38:9999"
    username = 'kqscyp4bkz-corp.mobile.res-country-NL-state-2743698-city-2747891-hold-session-session-6728e00108632:6AwTjJNpSE9n4exb'
    imag_count = 10

    proxies = {
        'http': f'http://nwlra1yqrz-corp.mobile.res-country-RU-state-524894-city-524901-hold-session-session-6728e5d0a317e:iHPs440r3LbXI5Q9@93.190.142.57:9999',
        'https': f'http://nwlra1yqrz-corp.mobile.res-country-RU-state-524894-city-524901-hold-session-session-6728e5d0a317e:iHPs440r3LbXI5Q9@93.190.142.57:9999'
    }

    for imag_num in range(imag_count):
        ans = req.get(link, proxies=None)
        extension = ans.headers['content-type'].split('/')[-1]
        filename = gener_filename(extension)

        with open(os.path.join('image', filename), 'wb') as file:
            file.write(ans.content)
        print(f'images: {imag_num + 1} finished..')

def gener_filename(file_extension):
    tmp = str(int(time.time()))
    for _ in range(5):
        tmp += chr(random.randint(65, 75))
    return f'{tmp}.{file_extension}'



if __name__ == '__main__':
    start = perf_counter()
    main()
    print(f'time: {(perf_counter() - start):.02f}')

