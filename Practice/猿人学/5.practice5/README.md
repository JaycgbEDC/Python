# 思路

* document.cookie = "RM4hZBv0dDon443M=" +  _0x4e96b4['_$ss'] + ';\x20path=/';  5次
  _0x4e96b4['_$ss'] = AES加密(_$Ww, _0x4e96b4["_$qF"])
* _$Ww=enc-utf8加密(_0x4e96b4['_$pr'])
  _0x4e96b4['_$pr']=[]，往数据加m的加密值  push了4次，有5个值
* document.cookie拿到值
  window._$is拿到请求参数m
  window.$_zw[23]拿到请求参数f

# 注意

间接使用eval作用域为全局，而沙箱就是这样的。例如此题b64pad会在eval中访问局部变量（值为window），访问不到会出错。所以以后要多检测eval中的东西。
