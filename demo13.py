# youxiue
# createTime: 2021/1/23 21:45
# 列表

'''
1. 列表元素按顺序有序排列
2. 索引映射唯一一个元素
3. 类别可以存储重复元素
4. 任意数据类型混存
5. 根据需要动态分配 和 回收内存
'''

# 第一种创建方式
lst = ['hello', 'world', 98, 'hello', 'jojo']

# 第二种创建方式, 使用内置函数 list()
lst2 = list(['hello', 'world', 98])

# 列表中查询操作
'''
index() 返回指定元素的索引
    1. 如过列表中存在N个相同元素, 只返回相同元素的第一个元素的索引
    2. 如果查询的元素在列表中不存在, 则会抛出 ValueError 异常
    3. 还可以在指定的 star 和 stop 之间进行查询 (含头不含尾)
'''
print(lst.index('world'))
# print(lst.index('python'))
print(lst.index('world', 1, 3))  #

'''
获取列表中的单个元素
    1. 正向索引 从 0  到 N-1, 例: lst[3]
    2. 逆向索引 从 -N 到 -1,  例: lst[-2]
    3. 指定索引不存在, 则会抛出 IndexError
'''
print(lst[0], lst[-2])

'''
获取列表中的多个元素 -- 切片
列表名[start: stop : step]
    切片的结果是 原列表片段的拷贝
    含头不含尾
    
    step 默认是1, 可简写为 [start, stop]
    
    step 是正数:   
        [:stop:step] -> 省略 start , start默认是列表的第一个元素,     从start 开始往后计算切片
        [start::step] -> 省略 stop , stop默认是列表的最后一个元素,   从start 开始往后计算切片
        
    step 是负数, (索引 start 和 stop 还是按正向0-N算):
        [:stop:step] -> 省略 start , start默认是列表的最后一个元素,     从start 开始往前计算切片
        [start::step] -> 省略 stop , stop默认是列表的第一个元素,   从start 开始往前计算切片
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[1:6:1])  # [2, 3, 4, 5, 6]
print(lst[1:6])  # [2, 3, 4, 5, 6] 默认步长为1
print(lst[1:6:])  # [2, 3, 4, 5, 6] 默认步长为1
print(lst[1:6:2])  # [2, 4, 6]
print(lst[:6:2])  # [1, 3, 5]
print(lst[3::2])  # [4, 6, 8]
print(lst[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst[:3:-1])  # [9, 8, 7, 6, 5]
print(lst[6::-1])  # [7, 6, 5, 4, 3, 2, 1]

'''
in 和 not in 可以判断列表中是否存在目标元素
'''
print(100 in lst)  # False
print(100 not in lst)  # True
print(5 in lst)  # True
print(5 not in lst)  # False

for item in lst: print(item, end='\t')
print()
'''
向列表中添加元素
    append(): 在列表的末尾添加一个元素
    extend(): 在列表的末尾至少添加一个元素, 批量添加
    insert(): 在列表的任意位置添加一个元素
    切片: 在列表的任意位置添加至少一个元素
'''
print(id(lst))
lst.append(100)
print(lst, id(lst))  # id并未发生变化
# lst.append(lst2) # 将lst2 作为一个元素 添加到了 lst 中
lst.extend(lst2)
print(lst)
lst.insert(2, 'in')
print(lst)  # [1, 2, 'in', 3, 4, 5, 6, 7, 8, 9, 100, 'hello', 'world', 98]
lst3 = ['kono', 'dioda', False]
lst[1:] = lst3
print(lst)  # [1, 'kono', 'dioda', False]

'''
从列表中删除元素
    remove():  一次删除一个元素
        重复元素只能删除第一个
        元素不存在则抛出 ValueError
    pop(): 删除一个指定索引位置上的元素
        不指定索引, 则删除最后一个元素
        指定索引不存在, 则抛出IndexError
    切片: 一次删除至少一个元素
    clear(): 清空元素
    del:  删除列表
    
'''
lst = [1, 2, 'j', 4, 4, 'k', 'jojo', 28, False, 'xixi']
lst.remove(4)
print(lst)
lst.pop(1)
print(lst)
# lst.pop(8)
lst.pop()
print(lst)
new_lst = lst[1:3]
print(new_lst)  #
print(lst)  # 原数组并没有新的变化, 只是 产生了一个新的数组

'''不产生新的列表对象, 而是删除原列表中的内容'''
lst[1:3] = []
print(lst)

lst.clear()
print(lst)

del lst
print(lst)  # 这里再调用会抛出异常  NameError
