import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('./pttMovie'):
    os.mkdir('./pttMovie')

url = 'https://www.ptt.cc/bbs/movie/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

for i in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    titleList = soup.select('div.title') # return List
    # print(titleList)

    for titleSoup in titleList:
        try:
            title = titleSoup.select('a')[0].text
            urlArticle = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
            resArticle = requests.get(urlArticle, headers=headers)
            soupArticle = BeautifulSoup(resArticle.text, 'html.parser')
            # Get article content
            articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站')[0]
            try:
                with open('./pttMovie/{}.txt'.format(title), 'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except FileNotFoundError as e:
                with open('./pttMovie/{}.txt'.format(title.replace('/', '-')), 'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except OSError as e:
                pass

            print(title)
            print(urlArticle)
        except IndexError as e:
            print(e)
            print(titleSoup)
        print('=============')

    # <a class="btn wide" href="/bbs/movie/index9512.html">‹ 上頁</a>
    urlNew = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    print(urlNew)
    url = urlNew