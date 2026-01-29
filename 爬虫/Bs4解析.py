# youxiue
# createTime: 2026/1/27

'''
bs4 是一个python库，用于解析HTML或XML文件

需要安装bs4  pip install bs4

'''


import requests
from bs4 import BeautifulSoup


domain = 'http://www.dygod.org'

dy_lst = []

# 获取首页信息
index_url = domain + '/index.htm'
resp = requests.get(index_url)
resp.encoding = 'gb2312'
html_content = resp.text

# 1. 把页面内容交给BeautifulSoup解析，生成bs对象
page = BeautifulSoup(html_content, 'html.parser')
# 2. 从bs中查找数据
# find(标签， 属性=值) 查找符合条件的第一个标签
# find_all(标签， 属性=值) 查找符合条件的所有标签，返回列表
# table = page.find("table", width="100%", border="0", cellpadding="0", cellspacing="0")
# 也可以使用attrs参数，传入一个字典
table = page.find("table", attrs={"width": "100%", "border": "0", "cellpadding": "0", "cellspacing": "0"})
# print(table)

# class是Python关键字， 所以用class_参数时要加下划线
tab_tds = table.find_all("td", class_="inddline") 
for td in tab_tds:
  a_tags = td.find_all("a")
  for a in a_tags:
    if a.text != '最新电影下载':
      link = a['href']
      title = a.text # 被标签包住的文本
      dy_lst.append({'title': title, 'link': domain + link})

  
print(dy_lst)
