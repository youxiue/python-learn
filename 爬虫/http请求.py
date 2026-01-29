# youxiue
# createTime: 2026/1/26

'''
爬虫: 

'''
import requests
from urllib.request import urlopen

# def get_html(url):
#     html = urlopen(url).read().decode('utf-8')
#     return html
  
# if __name__ == '__main__':
#   html = get_html('https://www.baidu.com')
#   print(html)



# query = input("请输入查询内容：")

# 获取网页信息
# url = f'https://www.baidu.com/s?wd=query={query}'
# h = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
# }
# print(requests.get(url, headers=h).text)
# res.close()

# 豆瓣排行榜
url = 'https://movie.douban.com/j/chart/top_list'
params = {
  'type': 11,
  'interval_id': '100:90',
  'action': '',
  'start': 0,
  'limit': 2
}
hd = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
}
res = requests.get(url, params=params, headers=hd)
print(res.json())
res.close()


# 使用百度翻译的接口
# url = 'https://fanyi.baidu.com/sug'
# data = {
#   'kw': query
# }
# res = requests.post(url, data=data)
# print(res.json())
res.close()

