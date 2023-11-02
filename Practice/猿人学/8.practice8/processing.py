# 图片预处理
import random
import os
from PIL import Image
from xin_fei_ocr import run_ocr
import numpy as np
import cv2


def turn_white(img, r1, g1, b1):
    """ 将部分像素值变为纯白色, r1, g1, b1 对应的rgb值 """
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = img.getpixel((i, j))
            if r == r1 and g == g1 and b == b1:
                img.putpixel((i, j), (255, 255, 255))



def noise_image(img_file):
    """选出rgb颜色最多2个，进行降噪处理"""
    img = Image.open(img_file)
    # colors所有像素rgb值，counts对应的数量
    colors, counts = np.unique(np.array(img).reshape(-1, 3), axis=0, return_counts=True)
    # 排序
    ct = np.sort(counts)
    # 找到出现最多的2种颜色的个数
    top2_counts = ct[-2:].tolist()
    # 找到出现最多的2种颜色的下标
    subscript_list = []
    for k, v in list(enumerate(counts, start=0)):
        if v in top2_counts:
            subscript_list.append(k)
    # 找到出现最多的2种颜色的rgb值
    for subscript in subscript_list:
        color = colors[subscript]
        # 去除颜色
        turn_white(img, color[0], color[1], color[2])
    return img


def interference(img_file):
    """移除干扰线条(通过选择字体间隔间的像素颜色，将对应颜色的像素都替换为白色)"""
    img = Image.open(img_file)
    # 读取图片高，宽
    height, width = img.height, img.width
    # 首先创建一个空列表,用来存放出现在间隔当中的像素点
    line_list = []
    # 两个for循环,遍历90000次
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 0 < y < 10 or 96 < y < 105 or 199 < y < 209 or 292 < y < 299:
                line_list.append([r, g, b])
            if 0 < x < 20 or 109 < x < 120 or 209 < x < 220:
                line_list.append([r, g, b])

    arr = np.array(line_list)
    line_list = np.array(list(set([tuple(t) for t in arr])))
    # 处理像素 RGB 值
    for line in line_list:
        r = line[0]
        g = line[1]
        b = line[2]
        if not (r == 255 and g == 255 and b == 255):
            turn_white(img, r, g, b)
    return img


def binary(img_file, standard=205):
    """灰度转换"""
    img = Image.open(img_file)
    img = img.convert('L')
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > standard:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img


def enhance(img_file):
    """增强字体显示效果(openCV的腐蚀方法，像素周围2×3区域只要有黑的，该像素值变为黑的)"""
    img = cv2.imread(img_file, 0)
    kernel = np.ones((2, 3), 'uint8')
    img = cv2.erode(img, kernel, iterations=2)
    return img


def image_clip(dir, img_file):
    """图片切割成单个字体便于识别"""
    img = cv2.imread(img_file, 0)
    clip_imgs = {}
    num = 1
    for y in range(0, 300, 100):
        for x in range(10, 300, 100):
            # 裁剪坐标为[y0:y1, x0:x1]
            cropped = img[y:y + 100, x:x + 100]
            cv2.imwrite(f"{dir}/f-{num}.jpg", cropped)
            res = run_ocr(f"{dir}/f-{num}.jpg")
            clip_imgs[res.rstrip()] = coordinate(num)
            num += 1
    return clip_imgs


def coordinate(num):
    """ 每张小图对应的坐标 """
    coordinate_dict = {
        1: random.randint(0, 9),
        2: random.randint(10, 19),
        3: random.randint(20, 29),
        4: random.randint(300, 309),
        5: random.randint(310, 319),
        6: random.randint(320, 329),
        7: random.randint(600, 609),
        8: random.randint(610, 619),
        9: random.randint(620, 629)
    }
    return coordinate_dict.get(num)


def run(path: str):
    dir = path.rsplit("/", 1)[0]
    image_a = noise_image(path)
    image_a.save(f'{dir}/noiseReduction.png')
    image_b = interference(f'{dir}/noiseReduction.png')
    image_b.save(f'{dir}/removeBar.png')
    image_c = binary(f'{dir}/removeBar.png')
    image_c.save(f'{dir}/grayConv.png')
    image_d = enhance(f'{dir}/grayConv.png')
    cv2.imwrite(f'{dir}/enhance.png', image_d)
    text_dict = image_clip(dir, f'{dir}/enhance.png')
    return text_dict


if __name__ == '__main__':
    path = './image/README/test.png'
    res = run(path)
    print(res)