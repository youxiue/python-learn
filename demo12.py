# youxiue
# createTime: 2021/1/23 21:25

# 输出一个三行四列的 * 矩形

for _ in range(3):
    for _ in range(4):
        print('*', end='\t')  # end='\t' 不换行输出
    print()

# 打印直角三角形
for i in range(1, 10):
    for j in range(1, i + 1):
        print('*', end='\t')
    print()

# 打印 9*9乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # print(str(j) + '*' + str(i) + '=' + str(i * j), end='\t')
        print(j, '*', i, '=', i * j, end='\t')
    print()
