# youxiue
# createTime: 2026/1/26
'''
死锁



'''

from threading import Thread, Lock

lockA = Lock()
lockB = Lock()

def task1():
    print('任务1 尝试获取锁A')
    lockA.acquire()
    print('任务1 获取到锁A')
    print('任务1 尝试获取锁B')
    lockB.acquire()
    print('任务1 获取到锁B')
    lockB.release()
    print('任务1 释放锁B')
    lockA.release()
    print('任务1 释放锁A')
    
def task2():
    print('任务2 尝试获取锁B')
    lockB.acquire()
    print('任务2 获取到锁B')
    print('任务2 尝试获取锁A')
    lockA.acquire()
    print('任务2 获取到锁A')
    lockA.release()
    print('任务2 释放锁A')
    lockB.release()
    print('任务2 释放锁B')
    

if __name__ == '__main__':
    t1 = Thread(target=task1)
    t2 = Thread(target=task2)
    t1.start()
    t2.start()