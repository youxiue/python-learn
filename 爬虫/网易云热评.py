# youxiue
# createTime: 2026/1/29
'''
爬虫.网易云热评 的 Docstring

Crypto需要安装 pip install pycryptodome

'''


from base64 import b64encode
import json 
import requests
from Crypto.Cipher import AES

token = 'e818c2d8ff785f8fcc2fe1cf09fc93c0'
url = f'https://music.163.com/weapi/comment/resource/comments/get?csrf_token={token}'



data = {
  "rid": "R_SO_4_3337300852",
  "threadId": "R_SO_4_3337300852",
  "pageNo": 2,
  "pageSize": 20,
  "cursor": -1,
  "offset": 0,
  "orderType": 1
}
i = '9ISCI9XVGVAMbvQM' # 固定值
e = "010001"
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
iv = '0102030405060708'
encSecKey = '30cac243df318abdba28914c829176a9600a3b0a4921cea87937dc332601dec5748454b6875c42c5b4d4b6e10af992e5dabe8d4d7407e5d545b7e996a33168392b45e637ab99fd88bbcb4a5acc1a7a46072540f11a72c1e996986d30793cb1f40c23bac344c252ae28101e34e5f9adb924659980a56007b2c932fab04927577f'

def pad(data):
  pad_num = 16 - len(data) % 16
  pad_str = chr(pad_num) * pad_num
  print('padStr: ' ,pad_str)
  return data + pad_str

#  数据 + g -> 结果 + i -> params
def toAes(data, key):
  cipher = AES.new(key = key.encode('utf-8'), mode = AES.MODE_CBC, iv = iv.encode('utf-8'))
  bs = cipher.encrypt(pad(data).encode('utf-8'))
  return str(b64encode(bs), 'utf-8')

def getParams(data):
  res = toAes(data, g)
  res = toAes(res, i)
  return res

requestBody = {
  'params': getParams(json.dumps(data)),
  'encSecKey': encSecKey
}

resp = requests.post(url, data=requestBody)
print(resp.json())