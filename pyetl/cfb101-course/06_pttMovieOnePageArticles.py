import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

titleList = soup.select('div.title') # return List
# print(titleList)

for titleSoup in titleList:
    title = titleSoup.select('a')[0].text
    urlArticle = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
    # print(titleSoup)
    # print(type(titleSoup.select('a')[0]))
    print(title)
    print(urlArticle)
    print('=============')