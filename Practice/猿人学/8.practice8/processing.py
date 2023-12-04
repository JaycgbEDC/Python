# 图片预处理
import random
import numpy as np
import cv2
from yinshua import run_ocr1
from matplotlib import pyplot as plt


def turn_white(img, b1, g1, r1):
    """ 将部分像素值变为纯白色, b1, g1, r1对应的BGR值 """
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            b, g, r = img[i, j]
            if r == r1 and g == g1 and b == b1:
                img[i, j] = [255, 255, 255]


def draw_hist(fileName):
    img = cv2.imread(fileName, 0)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def denoising(img_file):
    """选出rgb颜色最多2个(这个是经过直方图看出来的)，进行降噪处理"""
    img = cv2.imread(img_file, -1)
    colors, counts = np.unique(np.array(img).reshape(-1, 3), axis=0, return_counts=True)  # colors所有像素BGR值，counts对应的数量
    ct = np.sort(counts)  # 排序
    top2_counts = ct[-2:].tolist()  # 找到出现最多的2种颜色的个数
    # 找到出现最多的2种颜色的下标
    subscript_list = []
    for k, v in list(enumerate(counts)):
        if v in top2_counts:
            subscript_list.append(k)
    # 找到出现最多的2种颜色的BGR值
    for subscript in subscript_list:
        color = colors[subscript]
        turn_white(img, color[0], color[1], color[2])  # 去除颜色
    return img


def remove_lines(img_file):
    """移除干扰线条(通过选择字体间隔间的像素颜色，将对应颜色的像素都替换为白色)"""
    img = cv2.imread(img_file, -1)
    height, width = img.shape[0], img.shape[1]
    line_list = []  # 首先创建一个空列表,用来存放出现在间隔当中的像素点
    # 两个for循环,遍历90000次
    for x in range(width):
        for y in range(height):
            b, g, r = img[y, x]
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
            turn_white(img, b, g, r)
    return img


def binarization(img_file):
    """灰度转换"""
    img = cv2.imread(img_file, 0)
    _, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
    return img


def enhance(img_file):
    """增强字体显示效果(openCV的腐蚀方法，像素周围2×3区域只要有黑的，该像素值变为黑的)"""
    img = cv2.imread(img_file, 0)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 3))
    # kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    img = cv2.erode(img, kernel1)
    # img = cv2.dilate(img, kernel2, iterations=2)
    # img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations=2)
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
            res = run_ocr1(f"{dir}/f-{num}.jpg")
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


# def run(path: str):
#     dir = path.rsplit("/", 1)[0]
#     image_a = denoising(path)
#     cv2.imwrite(f'{dir}/denoising.png', image_a)
#     image_b = remove_lines(f'{dir}/denoising.png')
#     cv2.imwrite(f'{dir}/remove_lines.png', image_b)
#     image_c = binarization(f'{dir}/remove_lines.png')
#     cv2.imwrite(f'{dir}/binarization.png', image_c)
#     image_d = enhance(f'{dir}/binarization.png')
#     cv2.imwrite(f'{dir}/enhance.png', image_d)
#     text_dict = image_clip(dir, f'{dir}/enhance.png')
#     return text_dict


def run(path: str):
    dir = path.rsplit("/", 1)[0]
    """选出rgb颜色最多2个(这个是经过直方图看出来的)，进行降噪处理"""
    img = cv2.imread(path, -1)
    colors, counts = np.unique(np.array(img).reshape(-1, 3), axis=0, return_counts=True)  # colors所有像素BGR值，counts对应的数量
    ct = np.sort(counts)  # 排序
    top2_counts = ct[-2:].tolist()  # 找到出现最多的2种颜色的个数
    # 找到出现最多的2种颜色的下标
    subscript_list = []
    for k, v in list(enumerate(counts)):
        if v in top2_counts:
            subscript_list.append(k)
    # 找到出现最多的2种颜色的BGR值
    for subscript in subscript_list:
        color = colors[subscript]
        turn_white(img, color[0], color[1], color[2])  # 去除颜色

    """移除干扰线条(通过选择字体间隔间的像素颜色，将对应颜色的像素都替换为白色)"""
    height, width = img.shape[0], img.shape[1]
    line_list = []  # 首先创建一个空列表,用来存放出现在间隔当中的像素点
    # 两个for循环,遍历90000次
    for x in range(width):
        for y in range(height):
            b, g, r = img[y, x]
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
            turn_white(img, b, g, r)
    
    """灰度转换"""
    _, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)

    """增强字体显示效果(openCV的腐蚀方法，像素周围2×3区域只要有黑的，该像素值变为黑的)"""
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 3))
    img = cv2.erode(img, kernel)
    cv2.imwrite(f'{dir}/enhance.png', img)


if __name__ == '__main__':
    path = '/Users/kribe/Documents/Git/Python/Practice/猿人学/8.practice8/image/README/test.png'
    res = run(path)
    print(res)