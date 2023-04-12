import urllib.request, urllib.error
import re
import xlwt
import sqlite3
from bs4 import BeautifulSoup


pat_title = re.compile(r'<span class="title">(.*)</span>')
pat_score = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
pat_eva_number = re.compile(r'<span>(\d*)人评价</span>')
pat_overview = re.compile(r'<span class="inq">(.*)</span>')
pat_link = re.compile(r'<a href="(.*)">')
pat_img_link = re.compile(r'<img.*src="(.*?)"')  # ?表示非贪心
pat_actor = re.compile(r'<p class="">(.*?)</p>', re.S)


def ask_url(url):
    """ 获取数据：模拟浏览器根据url请求html网页
    :param url
    :returns: html 
    """
    html = ''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
    }
    req = urllib.request.Request(url, headers = headers)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(e)
    return html


def getdata(base_url):
    """ 获取豆瓣的top250电影的标题、评分、评价人数、简介、电影介绍链接、图片链接、演员等
    :param base_url
    :returns: list with 250 items like [[name_ch, name_en, score, eva_num, overview, film_link, film_img, film_actor], ...]
    """
    data_list = []
    for i in range(10):
        url = base_url + str(i * 25)
        html = ask_url(url)  # 模拟浏览器根据url请求html网页
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_ = 'item'):
            item = str(item)
            data = []
            titles = pat_title.findall(item)  # 添加电影的标题（中、英）
            if(len(titles) == 2):  # 若电影有中外标题
                data.append(titles[0])
                data.append(titles[1].replace('/', ''))
            else:  # 电影只有中文标题
                data.append(titles[0])
                data.append('中国大陆')
            scores = pat_score.findall(item)  # 添加电影的评分
            data.append(scores[0])
            eva_num = pat_eva_number.findall(item)  # 添加电影评价人数
            data.append(eva_num[0])
            overview = pat_overview.findall(item)  # 添加电影的简介
            if len(overview) == 0:
                data.append('暂无')
            else:
                data.append(overview[0].replace('。', ''))
            film_link = pat_link.findall(item)  # 添加电影的介绍链接
            data.append(film_link[0])
            film_img = pat_img_link.findall(item)  # 添加电影的图片链接
            data.append(film_img[0])
            film_actor = pat_actor.findall(item)[0].strip()  # 添加电影的演员类型等
            film_actor = re.sub(r'<br/>\s+', '', film_actor)
            data.append(film_actor)
            data_list.append(data)
    return data_list


def save_xls(data_list, path):
    """ 将数据保存为douban_top250.xls表 
    :param data_list: list with 250 items like [[name_ch, name_en, score, eva_num, overview, film_link, film_img, film_actor], ...]
    :param path: save path
    """
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 第二个参数表示压缩等级，默认为0，该参数不常用
    worksheet = workbook.add_sheet("top250", cell_overwrite_ok=True)  # 第二个参数表示单元格可被覆盖
    param = ('电影中文名称', '电影原产地名称', '评分', '评价人数', '电影简介', '电影详情链接', '电影图片链接', '电影演员、年份等')
    for j in range(len(param)):
        worksheet.write(0, j, param[j])
    for row, l in enumerate(data_list):
        for col, s in enumerate(l):
            worksheet.write(row + 1, col, s)
    workbook.save(path)


def init_db(path):
    """ 建表
    :param path
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    sql = '''
        create table movie250
        (id integer primary key autoincrement,
        movie_title_ch text,
        movie_title_origin text,
        score numeric,
        eval_num numeric,
        movie_info text,
        info_link text,
        img_link text,
        actor_year text
        )
    '''
    c.execute(sql)
    conn.commit()
    conn.close()


def save_db(data_list, path_db):
    """ 将数据保存到数据库
    :param data_list
    :param path_db
    """
    init_db(path_db)
    conn = sqlite3.connect(path_db)
    c = conn.cursor()
    for l in data_list:
        for i in range(len(l)):
            if i == 2 or i == 3:
                continue
            l[i] = '"' + l[i] + '"'
        sql = '''
            insert into movie250 (movie_title_ch, movie_title_origin, score, eval_num, movie_info, info_link, img_link, actor_year)
            values (%s)
        ''' % (','.join(l))
        c.execute(sql)
        conn.commit()
    conn.close()


def main():
    base_url = 'https://movie.douban.com/top250?start='
    # path_xls = r'./douban_top250.xls'
    path_db = r'./douban_top250.db'
    data_list = getdata(base_url)  # 获取网页内容
    # save_xls(data_list, path_xls)  # 保存为xls表
    save_db(data_list, path_db)
    

if __name__ == '__main__':
    main()