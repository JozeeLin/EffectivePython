#!/usr/bin/env python
# coding=utf-8

#import random.randint as randint
from random import randint
from collections import OrderedDict
from collections import defaultdict
from heapq import heappush,heappop


# 1================================
#a = {}
#a['foo'] =1
#a['bar'] = 2
## randomly populate 'b' to cause hash conflicts
#while True:
#    z = randint(99, 1013)
#    print(z)
#    b = {}
#    for i in range(z):
#        b[i] = i
#    b['foo'] = 1
#    b['bar'] = 2
#    for i in range(z):
#        del b[i]
#    if str(b) != str(a):
#        break


# 2================================
#a = OrderedDict()
#a['foo'] = 1
#a['bar'] = 2
#b = OrderedDict()
#b['foo'] = 'red'
#b['bar'] = 'blue'
#
#for value1, value2 in zip(a.values(), b.values()):
#    print(value1,value2)


# 3================================
#stats = {}
#key = 'my_counter'
#if key not in stats:
#    stats[key] = 0
#stats[key] += 1
#print(stats)


# 4================================
#stats = defaultdict(int)
#stats['my_counter'] += 1
#print(stats)


# 5================================
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
print(heappop(a),heappop(a),heappop(a),heappop(a))
