#!/usr/bin/env python
# coding=utf-8
from threading import Thread
from threading import Lock

class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


# 查询传感器读数的时候会发生阻塞式I/O操作,所以要给每个传感器分配自己的工作线程.每采集一次读数,工作线程就会给Counter对象的value值加1,然后继续采集,直至完成全部采样操作
def worker(sensor_index, how_many, counter): #how_many表示样本总数
    for _ in range(how_many):
        counter.increment(1)

#为每个传感器启动一条工作线程,然后等待它们完成各自的采样工作
def run_threads(func, how_many, counter):
    threads=[]
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

how_many = 10**5
# 1=================
#counter = Counter()

# 2===================
counter = LockingCounter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' % (5*how_many, counter.count))
