# 使用python执行js代码，对参数加密
# 网址：https://spa7.scrape.center/

import execjs
import json


item = {
    "name": '凯文-杜兰特',
    "image": 'durant.png',
    "birthday": '1988-09-29',
    "height": '208cm',
    "weight": '108.9KG'
}

file = "crypto.js"
node = execjs.get()  # 获取js执行环境
ctx = node.compile(open(file).read())  # CryptoJS声明好了

js = f"getToken({json.dumps(item, ensure_ascii = False)})"  # js语句
print(js)
result = ctx.eval(js)  # 执行js
print(result)