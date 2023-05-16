from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time


def lagou(url):
    """ 拉勾 """
    web = webdriver.Chrome()  # 打开chrome
    web.get(url)
    #  提取职位信息
    btn = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
    btn.click()
    time.sleep(2)
    web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python爬虫", Keys.ENTER)  # 找到文本框输入python爬虫, 点击搜索按钮
    time.sleep(1)
    ls = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
    for item in ls:
        name = item.find_element(By.XPATH, './div[1]/div[1]/div[1]/a').text
        date = item.find_element(By.XPATH, './div[1]/div[1]/div[1]/span').text
        salary = item.find_element(By.XPATH, './div[1]/div[1]/div[2]/span').text
        require = item.find_element(By.XPATH, './div[1]/div[1]/div[2]').text
        company = item.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text
        print(f"name: {name}\ndate: {date}\nsalary: {salary}\nrequire: {require}\ncompany: {company}")
        print("------------------------------------------------------------")

    #  iframe和多窗口调度
    web.find_element(By.XPATH, '//*[@id="openWinPostion"]').click()
    time.sleep(1)
    web.switch_to.window(web.window_handles[-1])
    job_detail = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
    print(job_detail)
    web.quit()


def endata(url):
    """ 无头浏览器：艺恩电影票房的select标签 """
    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    web = webdriver.Chrome(options = opt)  # 打开chrome
    web.get(url)
    # 切换select
    sel = Select(web.find_element(By.XPATH, '//*[@id="OptionDate"]'))
    for i in range(len(sel.options))[::-1]:
        sel.select_by_index(i)  # 按照索引位置切换
        time.sleep(1)
        table = web.find_element(By.XPATH, '//*[@id="TableList"]/table')
        print("==================================")
        print(table.text)


if __name__ == "__main__":
    url1 = "https://lagou.com"
    url2 = "https://www.endata.com.cn/BoxOffice/BO/Year/index.html"
    # lagou(url1)
    endata(url2)