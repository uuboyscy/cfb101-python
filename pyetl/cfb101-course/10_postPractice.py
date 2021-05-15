import requests

url = 'http://2280decc246b.ngrok.io/hello_post'
url = 'http://httpbin.org/post'
data = {
    'username': 'vhcjxzklhvcjxzkl'
}

res = requests.post(url, data=data)

print(res.text)