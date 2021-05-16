import requests
import json

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=235903762'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

res = requests.get(url, headers=headers)
# print(res.text)
jsonData = json.loads(res.text)  # list

for articleObj in jsonData:
    title = articleObj['title']
    articleUrl = 'https://www.dcard.tw/f/photography/p/' + str(articleObj['id'])
    print(title)
    print(articleUrl)
    for img in articleObj['mediaMeta']:
        imgUrl = img['url']
        print('\t', imgUrl)
    print('==========')
