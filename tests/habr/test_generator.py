import requests
from tqdm import tqdm

cnt = 0
for i in tqdm(range(450000, 453225)):
    response = requests.get('https://habr.com/ru/post/{0}/'.format(i))
    if response.status_code == 200:
        response.encoding = 'utf-8'

        file = open('tests_source/test{0}.html'.format(cnt), 'w')
        file.write(response.text)
        file.close()

        cnt += 1
