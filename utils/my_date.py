# youxiue
# createTime: 2026/1/21

'''
自定义日期模块

被模块包所引用
'''

import time

def get_day() -> str:
  return time.strftime("%Y-%m-%d", time.localtime())