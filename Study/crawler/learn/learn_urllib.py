import urllib.request


# 获取一个get请求，所用网址：http://httpbin.org
response = urllib.request.urlopen(r'http://www.baidu.com')
print(response.read().decode())


# 获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'yong院':'111'}), encoding = 'utf-8')
# response = urllib.request.urlopen(r'http://httpbin.org/post', data = data)
# print(response.read().decode())


# 超时处理
# try:
#     response = urllib.request.urlopen(r'http://httpbin.org/get', timeout=0.01)
#     print(response.read().decode())
# except urllib.error.URLError as e:
#     print("time out!")


# response的返回值
# response = urllib.request.urlopen(r'http://www.baidu.com')
# print(response.url, '\n', response.status, '\n', response.headers)


# 模拟浏览器请求网站
# url = 'https://www.baidu.com'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
# }
# req = urllib.request.Request(url = url, headers = headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode())