# youxiue
# createTime: 2026/1/21

'''
自定义时间模块

被模块包所引用
'''

import time

'''
获取当前时间
:return: 时间字符串
'''
def get_time():

    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  
def get_time_stamp():

    return time.time()  
