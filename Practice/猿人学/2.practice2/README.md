# 报错

* Fatal JavaScript invalid size error 184071938
  * 问题阐述：内存不足 超出了最大内存堆栈
  * 问题解决：检查下 代码中的格式化校验 搜索 `new regex` `.test` 然后后面的 `tostring`的那个函数，重新把前后格删掉即可或者恢复js压缩格式

# 思路

## 抓包

1. F12打开看看，发现无限debugger了，可以在这地方禁止断点
2. 可以看到数据在xhr请求中，携带的是page参数，返回的是想要的数据
3. 可以看到cookie是动态变化的，其中m值是变化的且加密，所以要寻找到m的加密

## hook到cookie

这里推荐个hook大全的网址：[hook大全](https://www.cnblogs.com/xiaoweigege/p/14954648.html "点我")

## 寻找m加密过程

1. 代码是经过sojson混淆过的，开头就是个大数组，很多十六进制数字，可以借助工具还原了，不还原也没关系
2. 把所有代码扣下来，运行会卡死，这里涉及到了sojson的格式化代码检测，可以hook掉
3. 然后就是缺啥补啥，注意补完后会报错：call需要一个函数，这里跟栈发现是setInterval作祟，因为这个函数需要两个参数，而第一个参数是undefined，所以可以把该行代码删除了，或者hook掉setInterval

## 知识点

* 无限debugger
* 动态cookie
* sojson格式化检测
