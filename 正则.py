# youxiue
# createTime: 2026/1/21

'''
正则

函数：
  compile(): 编译正则表达式

  match(pattern, str): 从字符串开头匹配
  search(pattern, str): 字符串中任意位置 开始查找，找到以一个就会返回
  findall(pattern, str): 查找所有匹配到的
  sub(pattern, 'newStr', str):   替换
  split(pattern, str): 分割

文档： https://docs.python.org/zh-cn/3/library/re.html#regular-expression-syntax

匹配模式
  . 任意字符 （除了\n)
  ^ 匹配字符串开头 行首
  $ 匹配字符串结尾(末尾如果有换行符\n, 就匹配\n前面的那个字符) 行尾
  () 一组 匹配小括号中的内容 (abc) 匹配的是abc这个整体  
  [] 范围 一个字符集合  [abc] 匹配的是a或b或c [a-z]
  [^ ] 非  [^abc] 匹配的不是a或b或c [^a-z]
  
正则预定义：
  \b 匹配单词边界
  \d 数字  [0-9]
  \D 非数字  [^0-9]
  \w 字母数字下划线  [a-zA-Z0-9_]
  \W 非字母数字下划线  [^a-zA-Z0-9_]
  \s 空格  [ \t\n\r\f\v]
  \S 非空格  [^ \t\n\r\f\v]
  
量词：
  * 匹配0个或多个 (贪婪匹配)
  + 匹配1个或多个 (贪婪匹配)
  ? 匹配0个或1个 惰性匹配
  {n} 匹配n个
  {n,} 匹配n个以上
  {n,m} 匹配n到m个
  
贪婪匹配：
  .* 匹配任意字符， 尽可能多的匹配
  .+ 匹配任意字符， 尽可能多的匹配
  .? 匹配任意字符， 尽可能少的匹配
  可以通过添加 ? 变成惰性匹配
  
  
分组
  正则使用()的部分，   通过result.group()获取组中的内容
'''
import re

t = '古力娜扎迪丽热巴马尔扎哈'
t1 = '马尔扎哈古力娜扎迪丽热巴马尔扎哈'

p = re.compile("马尔")

# match  只从头匹配， 匹配不到就返回None 
print(p.match(t)) # None 
print(p.match(t1)) # <re.Match object; span=(0, 2), match='马尔'> 

print(re.match("马尔", t1)) # <re.Match object; span=(0, 2), match='马尔'>

print(re.search("迪丽", t1)) # <re.Match object; span=(8, 10), match='迪丽'>

res = re.search("扎", t1)
print(res.span()) # (2, 3)  返回匹配的位置
print(res.group()) # 扎   提取匹配到的内容
print(res.groups())# ()   
 
msg = "2k323kj4545llsdlsg0fasas"
# 匹配开头字母中间数字结尾的字符串
res = re.findall('[a-z][0-9]+[a-z]' , msg)
print(res) # ['k323k', 'j4545l', 'g0f']

# 校验手机号
print(re.match('1[3-9]\d{9}$', '13521896742'))

# 校验用户名， 可以是字母或数字， 开头不能是数字， 长度6-16
p = re.compile('[a-zA-Z][a-zA-Z0-9]{5,15}$')
print(re.match(p, 'a21234abc')) # <re.Match object; span=(0, 9), match='a21234abc'>
print(re.match(p, 'a2123412334dsfgserwerw')) # None
print(re.match(p, 'a2123#@')) # None
# 可以有_， 长度6以上
p = re.compile('^[a-zA-Z][a-zA-Z0-9_]{5,}$')
print(re.match(p, 'a2123_3')) 

# 简写  \w 等同于 [a-zA-Z0-9_] 详情查看文档
p = re.compile('^[a-zA-Z]\w{5,}$')
print(re.match(p, 'a2123_3')) 

# 匹配所有的.py文件名
msg ='a.py sss.txt b.py www.video w*py c.py'
print(re.findall('\w+.py', msg)) # ['a.py', 'b.py', 'w*py', 'c.py']
print(re.findall(r'\w+\.py', msg)) # ['a.py', 'b.py', 'c.py']



# 校验邮箱 (word1|word1|word1) 表示的是一个单词或者多个单词， 和[]不一样，[]表示的是一个字符集合
p = re.compile(r'\w{5,20}@(163|qq|126|gmail)(\.\w+)+$')

# 检验邮箱 终极版
p = re.compile("^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
res = p.match('123@qq.com')
print(res)
print(p.match('123@qq.cn.qq.153.com'))


# qq号验证  5~11位 ，开头不能是0
p = re.compile('[1-9]\d{4,10}$')
print(p.match('123456789'))

# 分组 使用() 进行分组
# 获取电话的区号和 号码
res = re.match(r'^(\d{3,4})-(\d{7,8})$', '010-12345678')
print(res)
print(res.group(1)) # 010
print(res.group(2)) # 12345678
print(res.groups()) # ('010', '12345678')

# 分组 使用\number引用
msg = "<html><h1>标题</h1></html>"
res = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>', msg)
print(res)
print(res.groups()) # ('html', '<h1>标题</h1>')
res = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>', msg)
print(res)
print(res.groups()) # ('html', 'h1', '标题')

# 给正则取名字  (?P<name>正则) (?P=name)
msg = "<html><body><h1>标题</h1></body></html>"
res = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(res)  # <re.Match object; span=(0, 37), match='<html><body><h1>标题</h1></body></html>'>
print(res.group(1)) # html 
print(res.group(2)) # body
print(res.group(3)) # <h1>标题</h1>



# 替换
res =re.sub(r'\d+', '**', '语文成绩：89 数学成绩：90 英语成绩：80')
print(res) # 语文成绩：** 数学成绩：** 英语成绩：**

# 还可以传入函数，用函数处理
def func(temp):
  num = int(temp.group())
  num = num * 2
  return str(num)
res = re.sub(r'\d+', func, '语文成绩：89 数学成绩：90 英语成绩：80')
print(res) # 语文成绩：178 数学成绩：180 英语成绩：160

# 分割
res = re.split(r'\d+', '1a2b3c4d5e6f7g8h9i0j')
print(res) # ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(re.split(r'[,:]', '语文:88,数学:100')) # ['语文', '88', '数学', '100']

# 贪婪匹配
print(re.match(r'abc(\d+)', 'abc1234asss')) # <re.Match object; span=(0, 7), match='abc1234'>
# ? 通过添加？ 来改变贪婪匹配
print(re.match(r'abc(\d+?)', 'abc1234asss')) # <re.Match object; span=(0, 4), match='abc1'>


# 匹配图片路径
path = '<img data-v-d613d352="" src="https://i1.hdslb.com/bfs/banner/40c0ab656f59e615a7c01b23e329a57c6adb0aff.png@976w_550h_!web-home-carousel-cover" alt="你清醒一点！他只把你当棋子！" loading="eager" onload="fsrCb();firstSwipeLoaded(4)">'
res = re.match(r'<img.*?src="(.*?)"', path)
img_path = res.group(1)
print(res)
print(res.group(1))
import requests


response = requests.get(img_path)
with open('./file/bili_img.png', mode='wb') as fp:
  fp.write(response.content)