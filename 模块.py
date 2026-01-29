# youxiue
# createTime: 2026/1/21

'''
模块

语法
  1. import 模块名                         模块名.功能名
  2. import 模块名 as 别名                 别名.功能名
  3. from 模块名 import 功能名              功能名
  4. from 模块名 import 功能名 as 别名      别名
  5. from 模块名 import *                  功能名
      这个* 受到被导入包的 __all__ 的控制
'''

import random
print(random.randint(1, 10))


import math as m
print(m.sqrt(9))

from random import randint
print(randint(1, 10))

from random import randint as ri
print(ri(1, 10))

from random import *
print(random())


# 导入自定义的模块
import 自定义模块 as c
print(c.p)

print(c.circle_area(5))
print(c.circle_perimeter(5))
print(c.name())  # 模块名: 自定义模块
print(c.cylinder_volume(5, 10)) # 这里是可以用的

# 通过* 导入模块中的功能, 受到被导入模块的 __all__ 的控制
from 自定义模块 import *
print(circle_area(5))
# print(cylinder_volume(5, 10)) # 这里就会报错
