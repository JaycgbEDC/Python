# 思路

## 抓包

* 没有反调试操作，发现返回xhr数据只有三等奖的数据，没有总金额，那么再看网页源代码看有没有写死，发现并没有，于是就js中有没有处理内容，果然有，总金额=返回值的三等奖金额×24.
* 请求方式：Get；
* 携带参数：page、m和q
  * m动态变化
  * q也是动态变化的：page-时间戳|...
* cookie没有动态变化，估计给个sessionid就行了。

## 分析

* m = r(t, window.o)
  * t = Date.parse(new Date());
  * window.o就是page值
  * r函数再delect.js中
    * delect.js有一段AAEncode加密，把最后的括号'(_)'去掉，输入到控制台可以看到代码为：

      function anonymous() {window.o = 1}
    * 由此可以看到window.o搜不出来，原来是在这里加密了所以搜不到。
    * 此js还有一段webpack混淆
    * 1168有jsfuck加密，一堆中括号和感叹号，直接在网站解密即可。
* q = window.o + '-' + t + "|"

## 注意

* 服务器对q进行了严格校验，所以q和时间戳的生成最好是在python请求中请求，m的值在js中生成，即按照网页代码的逻辑来就行。
