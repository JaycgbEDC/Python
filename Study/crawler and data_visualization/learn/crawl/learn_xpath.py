# xpath 是在XML文档中搜索内容的一门语言
# html是xml的一个子集
from lxml import etree

def parse_xml():
    xml = """
    <book>
        <id>1</id>
        <name>野花遍地香</name>
        <price>1.23</price>
        <nick>臭豆腐</nick>
        <author>
            <nick id="10086">周大强</nick>
            <nick id="10010">周芷若</nick>
            <nick class="joy">周杰伦</nick>
            <nick class="jolin">蔡依林</nick>
            <div>
                <nick>热热热热热1</nick>
            </div>
            <span>
                <nick>热热热热热2</nick>
            </span>
        </author>

        <partner>
            <nick id="ppc">胖胖陈</nick>
            <nick id="ppbc">胖胖不陈</nick>
        </partner>
    </book>
    """
    tree = etree.XML(xml)
    # result = tree.xpath("/book")  # /表示层级关系. 第一个/是根节点
    # result = tree.xpath("/book/name")
    # result = tree.xpath("/book/name/text()")  # text() 拿文本
    # result = tree.xpath("/book/author//nick/text()")  # // 后代
    # result = tree.xpath("/book/author/*/nick/text()")  # * 任意的节点. 通配符(会儿)
    result = tree.xpath("/book//nick/text()")
    print(result)


def parse_html():
    tree = etree.parse(r"Study\crawler and data_visualization\learn\crawl\b.html")
    # result = tree.xpath('/html')
    # result = tree.xpath("/html/body/ul/li/a/text()")
    # result = tree.xpath("/html/body/ul/li[1]/a/text()")  # xpath的顺序是从1开始数的, []表示索引

    # result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # [@xxx=xxx] 属性的筛选

    # print(result)

    # ol_li_list = tree.xpath("/html/body/ol/li")
    #
    # for li in ol_li_list:
    #     # 从每一个li中提取到文字信息
    #     result = li.xpath("./a/text()")  # 在li中继续去寻找. 相对查找
    #     print(result)
    #     result2 = li.xpath("./a/@href")  # 拿到属性值: @属性
    #     print(result2)
    #
    # print(tree.xpath("/html/body/ul/li/a/@href"))

    print(tree.xpath('/html/body/div[1]/text()'))
    print(tree.xpath('/html/body/ol/li/a/text()'))


if __name__ == '__main__':
    parse_xml()
    parse_html()