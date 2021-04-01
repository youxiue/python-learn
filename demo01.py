# youxiue
# createTime: 2021/1/17 16:22

# 可以输出数字 字符串, 运算符表达式
print(520)
print(98.3)
print('hello world')
print("hello world")
print(4 + 1)

# ---------------------------------------------------------------------
# 将数据输出到文件中
# a: 以读写的方式 打开文件,  +: 追加模式, 不会覆盖之前的内容
# 1. 指定的盘符不能为空,
# 2. 使用 file = fp
fp = open('D:/python/open/demo01.txt', 'a+')
print('python 大法好', file=fp)
fp.close()

# ---------------------------------------------------------------------
# 转义字符 \
# \n 换行
print('hello\nworld')
# \t 制表符 tab
print('hello\tworld')  # 输出 hello  world
print('helloooo\tworld')  # 输出 helloooo	world
# \r 回车
print('hello\rworld')  # 输出 world , world 将 hello进行了覆盖
# \b 退格
print('hello\bworld')  # 输出 hellworld 退一格将 o退没了

print('http:\\\\www.baidu.com')  # http:\\www.baidu.com
print('子曰:\'学而时习之\'')  # 子曰:'学而时习之'

# 原字符, 不希望字符串汇总的转义字符起作用, 就使用原字符, 就是在字符串之前加上 r 或 R
print(r'hello\nworld')  # hello\nworld
# 使用原字符,  最后一个字符不能是\
# print(r'hello\nworld\') #报错
print(r'hello\nworld\\')  # 这样是可以的

# ---------------------------------------------------------------------
# 保留关键字
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# ---------------------------------------------------------------------
# 变量
name = 'zhangsan'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)


# ---------------------------------------------------------------------
# 数据类型
# 整数类型 int      98
# 二进制以0b开头,   八进制以0o开头,   十六进制 以0x开头
# 浮点数类型 float   3.14
# 布尔类型 bool     True,False
# 字符串类型 str     'hello'

# 使用 浮点数进行计算的时候, 可能会出现 小数位不确定的情况
print(1.1 + 2.2) # 3.3000000000000003
# 解决方案, 导入模块 Decimal
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))  # 3.3

# ---------------------------------------------------------------------
# 布尔型
f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))
print(f1 + 1)    # 2 说明True 表示1
print(f2 + 1)    # 1 说明False 表示0

# ---------------------------------------------------------------------
# 字符串  单个'  或 单个 " 只能在一行使用
str1 = '人生苦短, 我用python'
str1 = "人生苦短, 我用python"
# 三个'  或 三个" 可以多行使用
str1 = """人生苦短, 
我用python"""

str1 = '''人生苦短, 
我用python'''


# ---------------------------------------------------------------------
# 当剑str 类型与 int类型进行连接时, 需要将int转为 字符串类型
name = "小e"
age = 20
print(type(name), type(age))
# print('我叫'+name+',今年'+age+'岁') # 报错


# 使用 str() 将其他类型转为字符串类型
print('我叫'+name+',今年'+str(age)+'岁')
a = 198.8
b = False
print(str(a), str(b), type(str(a)), type(str(b))) # 198.8 False <class 'str'> <class 'str'>

# 使用 int() 将其他类型转为int类型
s1 = '129'
f1 = 98.7
s2 = '93.1'
ft = True
ff = False
s3 = 'hello'
print(int(s1), type(int(s1)))
print(int(f1), type(int(f1))) # 98 <class 'int'>
# print(int(s2), type(int(s2))) # 报错, 因为字符串为小数
print(int(ft), type(int(ft))) # 1
print(int(ff), type(int(ff))) # 0
# print(int(s3), type(int(s3))) # 报错,  将str 转为 int , 字符串必须为整数型字符串

#  使用 float() 将其他类型转为float 类型.
print(float(s1), type(float(s1))) # 129.0
print(float(f1), type(float(f1))) # 98.7
print(float(s2), type(float(s2))) # 93.1
print(float(ft), type(float(ft))) # 1.0
print(float(ff), type(float(ff))) # 0.0
# print(float(s3), type(float(s3))) # 报错,  将str 转为 float , 字符串必须为 小数型字符串


# 单行注释

''' 
多行注释
'''
"""
这也是多行注释
"""

# 可以在第一行声明编码格式
#coding:urf-8