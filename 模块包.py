# youxiue
# createTime: 2026/1/21

'''
模块包

导入方式
  1. import 包名.模块名
  2. from 包名 import 模块名
  3. from 包名 import *
  4. from 包名.模块名 import 功能名
  5. import 包名.模块名 import *
'''
# 方式1
# import utils.my_time
# print(utils.my_time.get_time())

# 方式2
# from utils import my_time
# print(my_time.get_time()) 

# 方式3 如果要使用该方式需要在包的__init__.py文件中添加__all__ = ['模块1', '模块2'....]
from utils import *
print(my_time.get_time()) # 使用 模块名.功能名
print(my_date.get_day())

# 方式4
from utils.my_time import get_time
print(get_time())

# 方式5
from utils.my_date import get_day
print(get_day())


