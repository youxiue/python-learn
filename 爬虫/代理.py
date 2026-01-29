# youxiue
# createTime: 2026/1/28

'''
代理 ： 访问一个网站，但是这个网站被墙了，那么我们就需要使用代理
 
可以从站大爷网站找免费代理IP  https://www.zdaye.com/
'''
import requests

proxies = {
    # 'http': 'http://127.0.0.1:8888',
    'http': 'http://47.92.242.45:8118'
}

resp = requests.get('https://www.baidu.com', proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
