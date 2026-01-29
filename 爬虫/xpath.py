# youxiue
# createTime: 2026/1/27

'''
xpath 是在XML中查找数据的一种语言

html是XML的子集

安装： pip install lxml
'''

from lxml import etree

xml = """
<books>
  <book id="1">
    <name>Python</name>
    <price>89.9</price>
    <author>
      <nick id="1001">周杰伦</nick>
      <nick id="1002">林俊杰</nick>
      <nick class="wlh">王力宏</nick>
      <div>
        <nick class="lrh">李荣浩</nick>
      </div>
      <span>
        <nick>林心如</nick>
      </span>
    </author>
  </book>
  <book id="2">
    <name>Java</name>
    <price>99.9</price>
    <author>javaer</author>
  </book>
</books>
"""

tree = etree.XML(xml)
res = tree.xpath('/books/book/name/text()')  # 查找所有book下的name标签的文本
print(res)  # ['Python', 'Java'] 
print(tree.xpath('/books/book/author/nick/text()')) # ['周杰伦', '林俊杰', '王力宏'] 
# 节点属性[@属性名="属性值"]
print(tree.xpath('/books/book/author/nick[@id="1002"]/text()')) # ['林俊杰']
print(tree.xpath('/books/book/author/nick[@class="wlh"]/text()')) # ['王力宏']
# 位置索引 从1开始
print(tree.xpath('/books/book/author/nick[2]/text()')) # ['林俊杰']
# // 表示查找所有子孙节点
print(tree.xpath('/books/book/author//nick/text()')) # ['周杰伦', '林俊杰', '王力宏', '李荣浩', '林心如']
# * 任意的节点，通配符
print(tree.xpath('/books/book/author/*/nick/text()')) # ['李荣浩', '林心如']

