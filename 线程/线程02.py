# youxiue
# createTime: 2026/1/26

'''
线程 是可以共享全局变量的

GIL 全局解释器锁
python 3.14之前的版本底层默认是加GIL锁的， 
但是3.14版本之后不再默认加锁，需要显示添加锁


线程： 适合I/O密集型操作， 网络操作， 文件读写
进程： 适合CPU密集型操作， 大量计算操作



'''
import threading


lock = threading.Lock()

ticket = 1000


def task(n):
    global ticket
    while True:
        # 写法一
        with lock:
            if ticket > 0:
                print('%s 卖票： %d' % (n, ticket))
                ticket -= 1
            else:
                break 
       
        # 写法二
        """ lock.acquire() # 请求锁
        if ticket > 0:
            print('%s 卖票： %d' % (n, ticket))
            ticket -= 1
        else:
            break
        lock.release() # 释放锁 """
          
          
if __name__ == '__main__':
    t1 = threading.Thread(target=task, args=('t1',))
    t2 = threading.Thread(target=task, args=('t2',))
    t3 = threading.Thread(target=task, args=('t3',))
    t1.start()
    t2.start()
    t3.start()