# youxiue
# createTime: 2021/1/23 18:07

a = int(input('a:'))
b = int(input('b:'))
'''
    if a>=b:
        print(a, '大于等于', b)
    else:
        print(a, '小于', b)
    
    
    if ... else 的简写格式
    
'''
print((str(a) + '大于等于' + str(b)) if a >= b else (str(a) + '小于' + str(b)))
