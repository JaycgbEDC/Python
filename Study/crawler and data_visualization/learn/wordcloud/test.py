import jieba  # 分词
import numpy as np  # 矩阵运算
import sqlite3  # 数据库
from matplotlib import pyplot as plt  # 绘图，数据可视化
from PIL import Image  # 图片处理
from wordcloud import WordCloud  # 词云


# 准备词云所需的文字（词）
text = ''
conn = sqlite3.connect(r'Study\crawler and data_visualization\DouBan\douban_crawl\douban_top250.db')
cur = conn.cursor()
sql = '''
    select movie_info from movie250
'''
for item in cur.execute(sql):
    text += item[0]
cur.close()
conn.close()


# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))


# 图片处理、生成词云
img = Image.open(r'Study\crawler and data_visualization\DouBan\douban_flask\static\img\tree.jpg')  # 打开遮罩图片
img_array = np.array(img)  # 将图片转换为数组
wc = WordCloud(
    background_color = 'white',
    mask = img_array,
    font_path = 'STXINGKA.TTF'  # 字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)


# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 是否显示坐标轴
# plt.show()  # 显示生成的词云图片(注意若此语句不注释，则下条语句的图片是白色的)


# 输出词云图片到文件
plt.savefig(r'.\Study\crawler and data_visualization\DouBan\douban_flask\static\img\word.jpg')