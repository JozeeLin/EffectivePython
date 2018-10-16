#!/usr/bin/env python
# coding=utf-8

from cProfile import Profile
from pstats import Stats


def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result

# 1==========================
#def insert_value(array, value):
#    for i, existing in enumerate(array):
#        if existing>value:
#            array.insert(i, value)
#            return
#    array.append(value)


# 2===========================
#from bisect import bisect_left
#def insert_value(array, value):
#    i = bisect_left(array, value)
#    array.insert(i, value)


from random import randint
max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)


profiler = Profile()
profiler.runcall(test)
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
