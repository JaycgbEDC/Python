# url: http://www.xinfadi.com.cn/priceDetail.html
import requests
import csv
from concurrent.futures import ThreadPoolExecutor


fp = open(r'Study\crawler and data_visualization\beijinxinfadi\data.csv', 'w', encoding = 'utf-8', newline='')  # 别漏了编码，否则写中文乱码，最后一个参数表示防止写的时候多写一行
csv_writer = csv.writer(fp)


def ask_url(data, i) -> list:
    """ 根据post请求的url返回结果并写入csv文件 """
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    response = requests.post(url, data = data)
    l = response.json()['list']
    for dic in l:
        save_l = [dic['prodCat'], dic['prodName'], dic['lowPrice'], dic['avgPrice'], dic['highPrice'], dic['specInfo'], dic['place'], dic['unitInfo'], dic['pubDate']]
        csv_writer.writerow(save_l)
    print(f'页面{i}爬取完成！')


def main():
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 22857):
            data = {
                'limit': '20', 
                'current': f'{str(i)}'
            }
            t.submit(ask_url, data = data, i = i)
    fp.close()


if __name__ == '__main__':
    main()