import requests
import wget
import os

from urllib.error import URLError
from time import sleep

f_s = 322
f_e = 322
o_s = 1
o_e = 10
page_s = 0
page_e = 1000

url = 'http://www.ogugauo.ru/funds/image.php?f={}&o={}&page={}'
images_dir = './images/'

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

error_count = 0
for f in range(f_s, f_e + 1):
    print('f:={}'.format(f))
    for o in range(o_s, o_e + 1):
        print('o:={}'.format(o))
        for page in range(page_s, page_e + 1):
            print('page:={}'.format(page))
            if not os.path.exists('{}{}_{}_{}.jpg'.format(images_dir, f, o, page)):
                try:
                    response = requests.request('GET', url.format(f, o, page))
                    if len(response.content) > 10:
                        print('Файл существует!')
                        filename = wget.download(url.format(f, o, page),
                                                 out='{}{}_{}_{}.jpg'.format(images_dir, f, o, page))
                        sleep(0.5)
                    else:
                        print('Файл не существует!')
                        break
                except ConnectionError as CE:
                    print(CE)
                    error_count = error_count + 1
                except requests.exceptions.ConnectionError as RECE:
                    print(RECE)
                    error_count = error_count + 1
                except requests.exceptions.ChunkedEncodingError as CEE:
                    print(CEE)
                    error_count = error_count + 1
                except URLError as UE:
                    print(UE)
                    error_count = error_count + 1
print('В ходе работы возникло {} ошибок.'.format(error_count))
