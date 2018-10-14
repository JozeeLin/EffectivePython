#!/usr/bin/env python
# coding=utf-8

from threading import Lock
import logging
from contextlib import contextmanager


# 1=============================
#lock = Lock()
#with lock:
#    print('Lock is held')
#
##等同于以下try/finally实现的方式
#lock.acquire() #锁请求
#try:
#    print('Lock is held') # 获得锁资源之后进入try语句块
#finally:
#    lock.release() #释放锁资源


# 2============================
def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')
#
#my_function()


# 3==============================
@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

#with debug_logging(logging.DEBUG):
#    print('Inside:')
#    logging.debug('hello logging')
#    #my_function()
#print('After:')
#my_function()


# 4==============================

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    myhandler = logging.StreamHandler()
    logger.addHandler(myhandler)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)
        #logger.removeHandler(myhandler)

with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!') #my-log logger
    logging.debug('This will not print')

logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
