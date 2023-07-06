# 由于不会写encSecKey密钥生成，所以encSecKey写死了
import requests
import string
import random
import json
from Crypto.Cipher import AES
from base64 import b64encode


def text_process(text):
    padding = 16 - len(text) % 16
    text += chr(padding) * padding
    return text


def generate_key(length):
    """ 生成length长度的密钥 """
    x = string.ascii_letters + string.digits
    return ''.join([random.choice(x) for _ in range(length)])


def aes_encrypt(d: bytes, g: bytes):
    encryptor = AES.new(key = g, mode = AES.MODE_CBC, iv = b"0102030405060708")
    return encryptor.encrypt(d)


def get_encSecKey():
    return "b5cad76b8deb55ae15948e2f6c0d2fe9024d598874926ee1570fe837e4acca10a9a4046e98cf0ef72850f33911f1fa6a7f01398589cf1cf0fdfd842e777f63b22f4bfa881b522226d7dce54593309052002c53e3a5be52377e4892484db92755f2b02b7268bd9f43c04f63f1338af3a4d330d47f788822a8f7e69b02061a2d5f"


def encrypt(d: str, g: bytes, i: str):
    h = {}
    # key_rand = generate_key(16)
    h['encText'] = text_process(str(b64encode(aes_encrypt(d.encode(), g)), 'utf-8')).encode()
    h['encText'] = str(b64encode(aes_encrypt(h['encText'], i.encode())), 'utf-8')
    h['encSecKey'] = get_encSecKey()
    return h


if __name__ == '__main__':
    d = {
        "csrf_token": "", 
        "rid": "R_SO_4_2039744487",
        "threadId": "R_SO_4_2039744487",
        "pageNo": 1,
        "pageSize": 20,
        "cursor": -1,
        "offset": 0,
        "orderType": 1
    }
    e = "010001"
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = "0CoJUm6Qyw8W8jud"
    i = "bDyzhrmQBe2AWufP"
    d = text_process(json.dumps(d))
    dic = encrypt(d, g.encode(), i)
    url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
    data = {
        "params": dic['encText'], 
        "encSecKey": get_encSecKey()
    }
    response = requests.post(url, data=data)
    print(response.text)