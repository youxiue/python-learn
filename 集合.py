# youxiue
# createTime: 2026/1/15

# 集合 set集合中不能存在相同的元素
s = {1, 2, 3}
print(s, type(s))

# s = {1, 2, "呵呵", [1, 2]} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s = {1, 2, "呵呵", (1, 2)}
print(s)

#不可哈希:python中的set集合进行数据存储的时候。需要对数据进行哈希计算，根据计算出来的哈希值进行存储数据
#        set集合要求存储的数据必须是可以进行哈希计算的。
#        可变的数据类型  list, dict, set

#可哈希:不可变的数据类型，int，str，tuple，bool.

# 创建空集合
s = set()
s.add(1)
s.add("张三")
s.add("李四")
s.add("fan")
print(s)

s.pop() # 由于set集合是无序的，所以每次取出的元素都是随机的
print(s)

s.remove("张三")
print(s)

# 没有修改里面的元素， 如果想修改只能删除，然后重新添加
s.remove("李四")
s.add("hong")
print(s)

for i in s:
    print(i)
    
# 交集 并集 差集
s1 = {1, 2, 3,}
s2 = {2, 3, 4, 5, 6}

# 交集
print(s1 & s2) # {2, 3}
print(s1.intersection(s2))
# 并集
print(s1 | s2) # {1, 2, 3, 4, 5, 6}
print(s1.union(s2))
# 差集
print(s1 - s2) # {1}
print(s2.difference(s1)) # {4, 5, 6}


# 可以利用不可重复性，去重
lst = ["1", "1","2", "2"]
print(set(lst)) # {'1', '2'}
print(list(set(lst))) # {'1', '2'}  无序的