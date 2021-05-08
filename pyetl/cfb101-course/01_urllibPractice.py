from urllib import request

url = 'http://ec2-13-113-4-216.ap-northeast-1.compute.amazonaws.com/hello_get?name=Allen'

res = request.urlopen(url=url)

html = res.read().decode('utf8')
print(html)