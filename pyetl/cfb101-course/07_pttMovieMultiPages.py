import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index{}.html'

page = 9513

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

for i in range(0, 5):
    print("++++++++++{}++++++++++++".format(i))
    res = requests.get(url.format(page), headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    titleList = soup.select('div.title') # return List
    # print(titleList)

    for titleSoup in titleList:
        try:
            title = titleSoup.select('a')[0].text
            urlArticle = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
            # print(titleSoup)
            # print(type(titleSoup.select('a')[0]))
            print(title)
            print(urlArticle)
        except IndexError as e:
            print(e)
            print(titleSoup)
        print('=============')

    page -= 1