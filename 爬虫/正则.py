# youxiue
# createTime: 2026/1/27
import re

s = """
<div class='gql'><span id='1'>郭麒麟</span></div>
<div class='yq'><span id='2'>于谦</span></div>
<div class='zyl'><span id='3'>张云雷</span></div>
<div class='zxy'><span id='4'>张学友</span></div>
<div class='zjl'><span id='5'>周杰伦</span></div>
<div class='wlh'><span id='6'>王力宏</span></div>
"""

# (?P<name>正则)  给分组起名字
pattern = re.compile(r"<div class='(.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S) # re.S 让 . 匹配包括换行符在内的所有字符

res = pattern.finditer(s)
for i in res:
    print(i.groups()) # ('gql', '1', '郭麒麟')
    print(i.group('id'), i.group('name')) # 1 郭麒麟
    print(i.group(1), i.group(2), i.group(3)) # gql 1 郭麒麟