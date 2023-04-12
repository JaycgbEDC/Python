from bs4 import BeautifulSoup


with open('./baidu.html', 'rb') as fp:
    html = fp.read()
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify)  # 缩进格式
    # print(bs.title)  # 获取title标签的所有内容
    # print(bs.title.name)  # 获取title标签的名称
    # print(bs.title.string)  # 获取title标签的文本内容
    # print(bs.head)  # 获取head标签的所有内容
    # print(bs.div)  # 获取第一个div标签中的所有内容
    # print(bs.div['id'])  # 获取第一个div标签的id的值
    # print(bs.a)  # 获取第一个a标签中的所有内容
    # print(bs.find_all('a'))  # 获取所有的a标签中的所有内容
    # print(bs.find(id = 'u1'))  # 获取id="u1"
    # print(type(bs.head))
    

    #1.Tag  标签及其内容；拿到它所找到的第一个内容

    # print(bs.title.string)
    #
    # print(type(bs.title.string))

    #2.NavigableString  标签里的内容（字符串)

    # print(bs.a.attrs)



    # print(type(bs))
    #3.BeautifulSoup   表示整个文档


    # print(bs.name)
    # print(bs)


    # print(bs.a.string)
    # print(type(bs.a.string))

    #4.Comment  是一个特殊的NavigableString ，输出的内容不包含注释符号


    #-------------------------------

    #文档的遍历

    # print(bs.head.contents)
    # print(bs.head.contents[1])

    #更多内容，搜索BeautifulSoup文档



    #文档的搜索

    # (1)find_all()
    # 字符串过滤：会查找与字符串完全匹配的内容
    # t_list = bs.find_all("a")

    # import re
    # 正则表达式搜索：使用search（）方法来匹配内容
    # t_list= bs.find_all(re.compile("a"))


    # 方法  ： 传入一个函数（方法),根据函数的要求来搜索  (了解）
    # def name_is_exists(tag):
    #     return tag.has_attr("name")
    #
    # t_list = bs.find_all(name_is_exists)
    #
    #
    # for item in t_list:
    #     print(item)

    # print(t_list)


    #2.kwargs   参数

    # t_list= bs.find_all(id="head")
    # t_list = bs.find_all(href="http://news.baidu.com")
    # t_list = bs.find_all(class_=True)

    # for item in t_list:
    #     print(item)


    #3.text参数

    # t_list= bs.find_all(text = "hao123")
    # t_list = bs.find_all(text =["hao123","地图","贴吧"])

    # t_list = bs.find_all(text = re.compile("\d"))  #应用正则表达式来查找包含特定文本的内容（标签里的字符串）


    #4.limit 参数

    # t_list = bs.find_all("a",limit=3)
    #
    # for item in t_list:
    #     print(item)


    #css选择器

    # t_list = bs.select('title')   #通过标签来查找

    # t_list = bs.select(".mnav")     #通过类名来查找

    # t_list = bs.select("#u1")   #通过id来查找

    # t_list = bs.select("a[class='bri']")  #通过属性来查找

    # t_list = bs.select("head > title")  #通过子标签来查找

    # t_list = bs.select(".mnav ~ .bri")

    # print(t_list[0].get_text())

    # for item in t_list:
    #     print(item)