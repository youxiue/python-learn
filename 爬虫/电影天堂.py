import requests
import re

domain = 'http://www.dygod.org'

dy_lst = []

# 获取首页信息
index_url = domain + '/index.htm'
resp = requests.get(index_url)
resp.encoding = 'gb2312'
html_content = resp.text
# print(html_content)

p_ul = re.compile(r'2023新片精品.*?<ul>(?P<ul_content>.*?)</ul>', re.S)
p_a = re.compile(r'<a href=\'(?P<link>.*?)\'>(?P<title>.*?)</a>', re.S)

# 先获取电影列表
ul_match = p_ul.finditer(html_content)
for ul in ul_match:
  ul_content = ul.group('ul_content')
  # 再获取每个电影的标题和链接
  a_match = p_a.finditer(ul_content)
  for a in a_match:
    link = a.group('link')
    title = a.group('title')
    # print(f"Title: {title}, Link: {link}")
    dy_lst.append({'title': title, 'link': domain + link})


# print(dy_lst)

p_download = re.compile(r'简　　介.*?<a.*?href="(?P<download_link>.*?)">', re.S)
# 获取下载链接
for dy in dy_lst:
  resp = requests.get(dy['link'])
  resp.encoding = 'gb2312'
  download_match = p_download.finditer(resp.text)
  for dl in download_match:
    download_link = dl.group('download_link')
    dy['download_link'] = download_link
    # print(download_link)
    
    
print(dy_lst)
  