# 知识点

* 开发者工具中header的内容不是原始header内容，它是根据键排序得到的，想要看到原始header，用抓包工具，该题检测了header的顺序
* 通过抓包发现，每次点击分页都会有两个请求，一个是请求图片返回sessionid，一个是得到数据，所以不能直接请求数据，要按先后顺序请求
* 为了保持会话，用requests库的session即可，另外requests会对header进行排序改变了原始header，所以要从底层覆盖header，也就是在session处覆盖
