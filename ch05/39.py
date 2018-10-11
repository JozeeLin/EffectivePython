#!/usr/bin/env python
# coding=utf-8

from queue import Queue
from threading import Thread
import time


# 1===========================
#queue = Queue()
#
#def consumer():
#    print('Consumer waiting')
#    queue.get()
#    print('Consumer done')
#
#thread = Thread(target=consumer)
#thread.start()
#
#print('Producer putting')
#queue.put(object())
#thread.join()
#print('Producer done')


# 2===============================
#queue = Queue(1)
#def consumer():
#    time.sleep(0.1) #给生产者流出一些时间
#    queue.get()
#    print('Consumer got 1')
#    queue.get()
#    print('Consumer got 2')
#
#thread = Thread(target=consumer)
#thread.start()
#
#queue.put(object())
#print('Product put 1')
#queue.put(object())
#print('Product put 2')
#thread.join()
#print('Product done')


# 3==================================
#in_queue = Queue()
#def consumer():
#    print('Consumer waiting')
#    work = in_queue.get()
#    print('Consumer working')
#    print('working ...')
#    print('Consumer done')
#    in_queue.task_done()
#
#Thread(target=consumer).start()
#
#in_queue.put(object())
#print('Producer waiting')
#in_queue.join()
#print('Producer done')


# 4===================================
def download(item):
    print('download:',item)


def resize(item):
    print('resize:',item)


def upload(item):
    print('upload:', item)


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return # Cause the thread to exit
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    '''生产者'''
    def __init__(self,func,in_queue,out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0


    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()

for _ in range(10):
    download_queue.put(object())

download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize(), 'items finished')
