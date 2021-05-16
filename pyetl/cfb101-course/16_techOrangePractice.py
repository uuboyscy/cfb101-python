import requests
import json
from bs4 import BeautifulSoup

url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

data = {
    'action': 'fm_ajax_load_more',
    'nonce': 'ab5d085223',
    'page': 1
}

for p in range(0,5):
    res = requests.post(url, headers=headers, data=data)

    jsonData = res.json()
    htmlStr = jsonData['data']
    # print(jsonData['data'])
    soup = BeautifulSoup(htmlStr, 'html.parser')

    # print(soup.select('h4 a'))
    for t in soup.select('h4 a'):
        print(t.text)
        print(t['href'])
        print('==========')

    data['page'] += 1
