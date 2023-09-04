import requests
import base64
import re
from fontTools.ttLib import TTFont
from lxml import etree


Base_api = f"https://match.yuanrenxue.cn/api/match/7"
proxy = "127.0.0.1:7890"
proxies = {
    "http": "http://" + proxy,
    "https": "http://" + proxy
}
name = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵']


def deal_woff(page, woff):
    # 下载woff文件并保存为xml格式
    data = base64.b64decode(woff)
    file_name = f"./{page}.woff"
    with open(file_name, 'wb') as f:
        f.write(data)
    font = TTFont(file_name)
    font.saveXML(f"./{page}.xml")
    # 解析xml文档
    _xml = etree.parse(f"./{page}.xml")
    map_value = {}
    for xm in _xml.xpath("//TTGlyph")[1:]:
        on_value = ''.join(xm.xpath('.//pt/@on'))
        key = str(xm.xpath("./@name")[0]).replace("uni", '')
        map_value[on_value] = key
    map_number = {
        '10100100100101010010010010': '0',
        '1001101111': '1',
        '100110101001010101011110101000': '2',
        '10101100101000111100010101011010100101010100': '3',
        '111111111111111': '4',
        '1110101001001010110101010100101011111': '5',
        '10101010100001010111010101101010010101000': '6',
        '1111111': '7',
        '101010101101010001010101101010101010010010010101001000010': '8',
        '10010101001110101011010101010101000100100': '9',
    }
    new_map_rs = {}
    for k, v in map_number.items():
        if map_value.get(k):
            new_map_rs[map_value.get(k)] = v

    return new_map_rs


def every_page(page, session, true_map):
    yyq = 1
    hero_name = []
    params = {
        'page': page
    }
    response = session.get(url = Base_api, params=params, proxies = proxies)
    woff = response.json()["woff"]
    data = response.json()["data"]
    font_l = [d["value"].replace("&#x", '').replace(' ', '') for d in data]
    map_rs = deal_woff(page, woff)
    for k, v in map_rs.items():
        font_l = re.sub(k, v, str(font_l))
    for _ in range(len(data)):
        hero_name.append(name[yyq + (page - 1) * 10])
        yyq += 1
    for zhs, sd in zip(hero_name, eval(font_l)):
        true_map[zhs] = sd


def crawl():
    true_map = {}
    session = requests.session()
    for i in range(5):
        every_page(i + 1, session, true_map)
    max_value = max(zip(true_map.values(), true_map.keys()))
    print(f"所以胜点最高的召唤师是{max_value[1]}，胜点为{max_value[0]}")


if __name__ == '__main__':
    crawl()