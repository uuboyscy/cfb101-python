import requests
from bs4 import BeautifulSoup

urlFirst = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
urlSecond = 'https://www.ptt.cc/ask/over18'
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

ss = requests.session()
print(ss.cookies)

resFirst = ss.get(urlFirst, headers=headers)
print(ss.cookies)
soupFirst = BeautifulSoup(resFirst.text, 'html.parser')
data = dict()

# print(soupFirst.select('input')[0])
data[soupFirst.select('input')[0]['name']] = soupFirst.select('input')[0]['value']
data[soupFirst.select('button')[0]['name']] = soupFirst.select('button')[0]['value']
print(data)

ss.post(urlSecond, headers=headers, data=data)
print(ss.cookies)

res = ss.get(url, headers=headers)
print(res.text)