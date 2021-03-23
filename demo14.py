# youxiue
# createTime: 2021/1/24 14:38

# 修改列表中的元素
lst = [10, 20, 30, 40]
# 一次修改一个值
lst[2] = 100
print(lst)
# 一次修改多个,  即将原本切片位置的值替换掉
lst[1:3] = [56, 78, 90, 340]
print(lst, id(lst))

# 排序
'''
 sort()  并不会产生新的对象, 是在原数组上排序的
'''
lst.sort()  # 默认升序排序
print(lst, id(lst))
'''
reverse=True 降序
reverse=False 升序
'''
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

'''
sorted() 会产生一个新的数组, 原数组不会变化
'''
lst = [875, 23, 52, 75, 12, 8565, 12234, 932, 43, 22]
newList = sorted(lst)
print(lst)
print(newList)
'''
    还是使用 reverse=True 降序
'''
descList = sorted(lst, reverse=True)
print(descList)


lst = ['jo', '啥', '23', 37, False, '哈']
# lst.sort() # 将会报错 TypeError: '<' not supported between instances of 'int' and 'str'
print(lst)



'''
列表生成式  [列表元素表达式(通常包含自定义变量) for 自定义变量 in 可迭代对象]
'''
lst = [i for i in range(1, 10)]
print(lst) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [i*i for i in range(1, 10)]
print(lst) #[1, 4, 9, 16, 25, 36, 49, 64, 81]
lst = [i*2 for i in range(1, 6)]
print(lst) #[2, 4, 6, 8, 10]