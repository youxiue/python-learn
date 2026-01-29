# youxiue
# createTime: 2026/1/26

'''
线程

线程是操作系统能够进行运算调度的最小单位， 是程序执行流的最小单元， 一个进程可以包含多个线程

状态： 新建、就绪、运行、阻塞、终止

'''

import threading
from time import sleep


def download(n):
  images = ['apple.jpg', 'banana.jpg', 'orange.jpg', 'pear.jpg']
  for image in images:
    print('正在下载：', image)
    sleep(n)
    print('下载完成：', image)

def listenMusic(n):
  songs = ['一路向北', '菊花台', '东风破', '龙卷风']
  for song in songs:
    print('正在播放：', song)
    sleep(n)
    print('播放完成：', song)
    
    
if __name__ == '__main__':
  
  t1 = threading.Thread(target=download, args=(1,))
  
  t2 = threading.Thread(target=listenMusic, args=(1,))
  
  t1.start()
  
  t2.start()