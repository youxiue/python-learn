# youxiue
# createTime: 2026/1/28

import requests
from lxml import etree

url = 'http://www.dygod.org/index.htm'
resp = requests.get(url)
resp.encoding = 'gb2312'
html = resp.text
# print(html)

# with open('./file/dygod.html', mode='w', encoding='utf-8') as fp:
#   fp.write(html)

etree = etree.HTML(html)
# 获取最新电影
newDys = etree.xpath('/html/body/div/div/div[3]/div[2]/div[1]/div/div[2]/ul/a/text()')
# print(newDys)

# ！！！！！！！！！ 妈的， 网页源码上有table下面有tbody标签，下载下来才发现实际上是没有的， 找半天原因
                  
print(etree.xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[1]/form/div[1]/p[1]/strong/text()'))
# trs = etree.xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/tbody/tr')
print(etree.xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/@class'))
print(etree.xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/@width'))
                  # '/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/tbody/tr[1]'
                  

print(etree.xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/tr[1]/td[1]/@width'))
trs = etree.xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/tr')
print(len(trs))
# for tr in trs:
#   print(tr.xpath('./td[1]/a[2]/text()'))
#   print(tr.xpath('./td[2]/font/text()'))

                      
rhDys =etree.xpath('/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div/div[5]/div[2]/ul/table/tr')
print(len(rhDys))
# 获取日韩电视剧
for dy in rhDys:
  print(dy.xpath('./td[1]/a[2]/text()'))
  print(dy.xpath('./td[2]/font/text()'))



# 获取游戏
                  # '//*[@id="header"]/div/div[3]/div[2]/div[3]/div[1]/div/div[3]/div[2]/ul/table/tbody'
                  # '/html/body/div/div/div[3]/div[2]/div[3]/div[1]/div/div[3]/div[2]/ul/table/tbody/tr[1]'
youxis = etree.xpath('/html/body/div/div/div[3]/div[2]/div[3]/div[1]/div/div[3]/div[2]/ul/table/tr')
for youxi in youxis:
  print(youxi.xpath('./td[1]/a[2]/text()'))
  print(youxi.xpath('./td[2]/font/text()'))




