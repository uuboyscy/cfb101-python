import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)

logo = soup.select('a#logo')
logo = soup.select('a[id="logo"]')
print(logo)
print(logo[0])
print(logo[0].text)
print('https://www.ptt.cc' + logo[0]['href'])
print(logo[0]['id'])

bbsContent = soup.select('div.bbs-content')
print(bbsContent)

