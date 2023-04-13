import sqlite3
import urllib.request, urllib.error
import os


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
}


def get_link(path_db):
    """ 获取数据中的图片名称以及链接
    :param path_db
    :returns: a list like [(name_ch, img_link), (name_ch, img_link),...]
    """
    conn = sqlite3.connect(path_db)
    cur = conn.cursor()
    sql = '''
        select movie_title_ch, img_link from movie250
    '''
    records = cur.execute(sql)
    l = records.fetchall()
    cur.close()
    conn.close()
    return l


def crawl_save(link_list, save_dir):
    """ 爬取并保存 
    :param link_list
    :param save_dir
    """
    if not os.path.exists(save_dir):  # 如果存储图片的文件夹不存在
        os.mkdir(save_dir)
    for t in link_list:
        suffix = t[1].split('.')[-1]
        path = save_dir + t[0] + '.' + suffix
        try:
            req = urllib.request.Request(url = t[1], headers = headers)
            response = urllib.request.urlopen(req)
            with open(path, 'ab') as fp:
                fp.write(response.read())
        except BaseException as e:
            print(e.reason)
    print('爬取完毕！')


def main():
    path_db = r'./douban_top250.db'  # 数据库的路径
    save_dir = r'./img_top250/'  # 存储图片的文件夹路径
    link_list = get_link(path_db)
    crawl_save(link_list, save_dir)


if __name__ == '__main__':
    main()