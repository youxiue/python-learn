# youxiue
# createTime: 2026/1/26

'''
进程通信


'''
from multiprocessing import Process, Queue
from time import sleep


'''
队列
'''
q = Queue(3)

# 添加数据
q.put('a')
q.put('b')
q.put('c')
print(q.qsize())
# q.put('d') # 如果队列已满，会阻塞， 直到队列有空位
# q.put_nowait('d') # 如果队列已满， 抛出异常 queue.Full
# q.put('d', timeout=2) # 队列满，阻塞2秒， 2秒后如果队列还是满， 抛出异常 queue.Full
if q.full():
    print('队列已满')
else:
    q.put('d')

# 取出数据
print(q.get())
print(q.get())
print(q.get())
print(q.qsize())
# print(q.get()) # 如果队列为空， 会阻塞， 直到队列有数据
# print(q.get_nowait()) # 如果队列为空， 抛出异常 queue.Empty _queue.Empty
# print(q.get(timeout=3)) # 队列空， 阻塞3秒， 3秒后如果队列还是空， 抛出异常 queue.Empty


# 使用 Queue 实现进程间通信


def download(fileQueue):
  images = ['apple.jpg', 'banana.jpg', 'orange.jpg', 'pear.jpg']
  for image in images:
    fileQueue.put(image)
    print('正在下载：', image)
    sleep(1)

def getFile(fileQueue):
  while True:
    try:
      image = fileQueue.get(timeout=5)
      print('处理完成：', image)
    except Exception as e:
      break
  
  
if __name__ == '__main__':
  fileQueue = Queue(3)
  p1 = Process(target=download, args=(fileQueue,))
  p2 = Process(target=getFile, args=(fileQueue,))
  p1.start()
  p2.start()
  p1.join()
  p2.join() 