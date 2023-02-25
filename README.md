# 关于做题过程中不熟悉的函数进行的总结

## 基础语法

### 深浅拷贝

* python基于值管理，如a=2表明a指向值为2的内存空间，若a += 1，则a改变指向，也就是取出a的值加一放于新内存，a指向新内存
* 深拷贝：a = b = 1，就是a拷贝了b的值，若b改变值，a不会变
* 浅拷贝：a = b = []，b若改变，a会跟着一起改，这个时候可以
* 参考文章：[深浅拷贝](https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html "click")

## 正则表达式

### 基础语法

1. 注意{m,n}中间不能有空格

## 内置函数

### divmod

* divmod(a, b)：返回一个包含商和余数的元组(a // b, a % b)

## 序列部分

### 列表

1. 创建空列表：注意list(d)，d是字典时，返回的是d的key值列表
2. 列表切片返回相反列表：l[::-1]

### 集合

1. 创建空集合：set()，注意不是{}（字典可用{}）

## 模块部分

### Random模块

1. random.random(): 产生[0, 1)之间浮点数
2. random.randint(a, b): 产生[a, b]之间随机整数
3. random.uniform(a, b): 产生[a, b]之间随机浮点数
4. random.shuffle(x): 打乱序列x的顺序

### datetime库

* datetime库包含了四个类型：datetime、date、time、timedelta，分别表示日期+时间、日期、时间、时间差
* 对象可用months、days、seconds返回年、月、日

#### datetime类型

1. datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])，返回年月日、时分秒（需print打印出来）
2. datetime.datetime().now()：返回当前系统时间
3. datetime.datetime. **strftime** ()：由日期格式转化为字符串格式
   * datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')：'Feb-20-2023 17:53:06'
4. datetime.datetime. **strptime()** ：由字符串格式转化为日期格式
   * datetime.datetime.strptime('Feb-20-2023 17:53:06', '%b-%d-%Y %H:%M:%S')：datetime.datetime(2023, 2, 20, 17, 53, 6)

### collections库

* collections.__all__查看所有的子类，一共包含9个

#### Counter

* 计数器，是dict的子类，用于**计数可哈希对象**，它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值
* Counter(list)：统计list中元素个数，返回字典

## 文件操作部分

1. open('文件名', mode)：mode可为r、w，b表示二进制文件
   * r和w都会将文件指针放在开头，即文件存在就删除所有内容，不存在就创建
   * +号可与rw结合，如与r+、w+表可读可写
   * a是追加模式，文件指针会放在文件末尾
2. 文件对象方法：
   * readline读一行，readlines读每一行返回列表
   * write(s)表示把s写入文件，**不会加换行**，writelines(l)把字符串列表l写入文件，也不加换行
