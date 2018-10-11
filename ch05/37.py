#!/usr/bin/env python
# coding=utf-8

from time import time
from threading import Thread
import select

#numbers = [2139079, 1214759, 1516637, 1852285]
#
#def factorize(number):
#    for i in range(1, number+1):
#        if number % i == 0:
#            yield i
#
# #1===============================
#start = time()
#for number in numbers:
#    list(factorize(number))
#end = time()
#
#print('Took %.3f seconds' % (end-start))
#
## 2=============================
#class FactorizeThread(Thread):
#    def __init__(self, number):
#        super().__init__()
#        self.number = number
#
#    def run(self):
#        self.factors = list(factorize(self.number))
#
#start = time()
#threads = []
#for number in numbers:
#    thread = FactorizeThread(number)
#    thread.start()
#    threads.append(thread)
#
#for thread in threads:
#    thread.join()
#
#end = time()
#print('Took %.3f seconds' % (end-start))


# 3==================================
def slow_systemcall():
    select.select([],[],[],0.1)

#start = time()
#for _ in range(5):
#    slow_systemcall() #此处程序的主线程会卡在select系统调用那里.
#end = time()
#print('Took %.3f seconds' % (end-start))


# 4===============================================
start = time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end-start))
