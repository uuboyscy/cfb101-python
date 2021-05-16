import json
import requests

jsonStr = ''
with open('test.json', 'r', encoding='utf-8') as f:
    jsonStr = f.read()

jsonData = json.loads(jsonStr)

# for i in jsonData:
#     print(i)

res = requests.get('https://www.dcard.tw/service/api/v2/posts?popular=true&limit=30&before=235984417')
print(res.text)
