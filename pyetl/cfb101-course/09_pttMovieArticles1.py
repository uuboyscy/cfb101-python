import requests
from bs4 import BeautifulSoup

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