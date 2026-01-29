# youxiue
# createTime: 2026/1/27

import requests
import re

url = 'https://movie.douban.com/top250'
hd = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
}
res = requests.get(url, headers=hd)
page_content = res.text
# print(page_content)
res.close()

p = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)</span>.*?'
               r'<div class="bd">.*?<br>(?P<year>.*?)&nbsp.*?'
               r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
               r'<span>(?P<ratings>\d+)人评价</span>'
               , re.S)

cw = open('file/douban_top250.csv', 'w', encoding='utf-8')
for item in p.finditer(page_content):
  # print(item.group('title'), item.group('year'), item.group('score'), item.group('ratings'))
  cw.write(f"{item.group('title').strip()},{item.group('year').strip()},{item.group('score')},{item.group('ratings')}\n")
