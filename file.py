# youxiue
# createTime: 2026/1/15

import os # 和操作系统模块相关的模块

'''
open(
    file,
    mode='r',
    encoding=None
)
file: 文件路径
    1. 绝对路径
    2. 相对路径
mode: 模式
    r: 只读
    w: 只写
    a: 追加
    b: 二进制模式, 打开非文本文件的时候

with: 创建一个上下文管理器，自动调用close()方法
    

'''

fr = open('./file/file_text.text', mode='r', encoding='utf-8')

# 一次性读取整个文件，不建议这么做，如果文件过大，可能会导致内存溢出
# content = fr.read()
# print(content)

# 按行读取  strip()是去掉两段的空白，空格，换行，制表符
# line1 = fr.readline().strip()
# print(line1)

# 读取所有行，返回的是一个列表
# lines = fr.readlines()
# print(lines)

for line in fr.readlines():
    print(line.strip())
    
fr.close()


# 写入模式 w
# 如果文件不存在，则创建
# 每一次open都会清空之前的内容
fw = open('./file/file_w.text', mode='w', encoding='utf-8')
fw.write('hello world')

lst = ['python', 'java', 'c', 'c++', 'c#', 'go', 'rust', 'swift', 'kotlin', 'scala']
for item in lst:
    fw.write(item + '\n')

fw.close()


# 追加模式 a
# 不再清空之前的内容，只会追加
fa = open('./file/file_a.text', mode='a', encoding='utf-8')
for item in lst:
    fa.write(item + '\n')
    
fa.close()

# 安全的打开模式， 结束后自动调用close()关闭 ， 确保文件关闭
with open('./file/file_a.text', mode='r', encoding='utf-8') as fp:
    print(fp.read())


# 读取图片
# 在读取非文本文件时，需要使用二进制模式打开 加上b
# with open('./file/apple.jpg', mode='rb') as fp:
#     content = fp.read()
    # print(content)
    
    
# 文件的复制
# with open('./file/apple.jpg', mode='rb') as frb, \
#      open('./file/apple_copy.jpg', mode='wb') as fwb:
#     while True:
#         content = frb.read(1024)
#         if not content:
#             break
#         fwb.write(content)

# 文件的修改， 可以通过读取文件，然后修改，写入复制文件，再删除源文件，更改负责文件名为源文件名
with open('./file/file_w.text', mode='r', encoding='utf-8') as fr, \
     open('./file/file_w_copy.text', mode='w', encoding='utf-8') as fw:
       for line in fr.readlines():
           if 'java' in line:
               line = line.replace( 'java', 'python')
           fw.write(line)
           
# 删除原文件
os.remove('./file/file_w.text')
# 修改文件名 把copy文件名改为原文件名
os.rename('./file/file_w_copy.text', './file/file_w.text')