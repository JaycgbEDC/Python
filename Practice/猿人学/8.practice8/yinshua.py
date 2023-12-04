
"""
  印刷文字多语种识别WebAPI接口调用示例接口文档(必看)：https://doc.xfyun.cn/rest_api/%E5%8D%B0%E5%88%B7%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB%EF%BC%88%E5%A4%9A%E8%AF%AD%E7%A7%8D%EF%BC%89.html
  图片属性：尺寸1024×768，图像质量75以上，位深度24最短边最小不低于20像素，最大不超过4096像素，格式jpg/jpeg
  (Very Important)创建完webapi应用添加服务之后一定要设置ip白名单，找到控制台--我的应用--设置ip白名单，如何设置参考：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=41891
  错误码链接：https://www.xfyun.cn/document/error-code (code返回错误码时必看)
  @author iflytek 
"""
#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json
from xin_fei_ocr import run_ocr2


#  印刷文字多语种 webapi接口地址
URL = "http://webapi.xfyun.cn/v1/service/v1/ocr/recognize_document"
#  应用ID (必须为webapi类型应用，并印刷文字识别多语种服务，参考帖子如何创建一个webapi应用：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=36481)
APPID = "90da4be6"
#  接口密钥(webapi类型应用开通印刷文字识别多语种服务后，控制台--我的应用---印刷文字识别多语种---服务的apikey)
API_KEY = "f7ec478255f577ffabe91e2904c602f9"
def getHeader():
    curTime = str(int(time.time()))
    param = {"engine_type": "recognize_document"}
    param = json.dumps(param)
    paramBase64 = base64.b64encode(param.encode('utf-8'))
    m2 = hashlib.md5()
    str1 = API_KEY + curTime + str(paramBase64,'utf-8')
    m2.update(str1.encode('utf-8'))
    checkSum = m2.hexdigest()
    #   组装http请求头
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


def run_ocr1(file_path):
    #  上传图片路径，base64编码后大小不超过4m
    with open(file_path, 'rb') as f:
        f1 = f.read()
    f1_base64 = str(base64.b64encode(f1), 'utf-8')    
    data = {
            'image': f1_base64
    }
    r = requests.post(URL, data=data, headers=getHeader())
    if not r.json()["data"]["document"]["blocks"]:
        result = run_ocr2(file_path)
    else:
        result = r.json()["data"]["document"]["blocks"][0]["lines"][0]["characters"][0]["text"]
    # 错误码链接：https://www.xfyun.cn/document/error-code (code返回错误码时必看)
    return result


if __name__ == '__main__':
    file_path = "/Users/kribe/Documents/Git/Python/Practice/猿人学/8.practice8/image/README/f-3.jpg"
    res = run_ocr1(file_path)
    print(res)