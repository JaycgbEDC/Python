# 代理爬虫  https://www.zdaye.com/free/
import requests


proxies = {
    'http': 'http://47.97.97.119:3128'
}
response = requests.get('https://www.baidu.com', proxies = proxies)
response.encoding = 'utf-8'
print(response.text)