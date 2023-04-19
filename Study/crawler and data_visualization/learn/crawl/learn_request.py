import requests


# # 搜狐的get请求
# query = input('请输入你需要搜索的明星：')
# url = f'https://www.sogou.com/web?query={query}'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
# }
# response = requests.get(url, headers=headers)
# print(response.text)


# # 百度翻译的post请求
# word = input('请输入要查询的词：')
# url = 'https://fanyi.baidu.com/sug'
# data = {
#     'kw': word
# }
# response = requests.post(url, data = data)
# print(response.json()['data'][0]['v'])  # 返回值是json 那就可以直接解析成json


# # 抓取豆瓣电影排行榜-喜剧电影
# url = 'https://movie.douban.com/j/chart/top_list'
# params = {
#     'type': '24', 
#     'interval_id': '100:90', 
#     'action': '', 
#     'start': '0',  # 从库中的第几部电影去取
#     'limit': '20'  # 一次取出的个数
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
# }
# response = requests.get(headers=headers, url=url, params=params)
# print(response.request.url)
# # print(response.json())
# response.close()


# 请求加密的html
url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}
response = requests.get(url, headers=headers, verify=False)
print(response.text)