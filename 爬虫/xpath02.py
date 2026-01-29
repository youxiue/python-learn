# youxiue
# createTime: 2026/1/27

from lxml import etree

tree = etree.parse('./file/xpath_test.html')

# print(tree.xpath('/html/body/ul/li/a/text()'))
# print(tree.xpath('/html/body/ul/li[2]/a/text()'))
# print(tree.xpath('/html/body/ul/li/a[@href="https://www.taobao.com"]/text()'))
print(tree.xpath('/html/body/ol/li[2]/a'))


ol_li_lst = tree.xpath('/html/body/ol/li')
print(len(ol_li_lst))
for li in ol_li_lst:
    print(li.xpath('./a/text()'))  # ./ 表示当前节点
    print(li.xpath('./a/@href'))  # 获取属性值
