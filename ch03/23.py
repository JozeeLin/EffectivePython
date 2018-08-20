#!/usr/bin/env python
# coding=utf-8
from collections import defaultdict

current = {'green':12,'blue':3}
increments = [('red',5),('blue',17),('orange',9),]

##使用函数作为钩子
#def log_missing():
#    print('key added')
#    return 0
#result = defaultdict(log_missing, current)
#print('Before:', dict(result))
#for key, amount in increments:
#    result[key] += amount
#print('After:', dict(result))

##使用闭包作为钩子
#def increment_with_report(current, increments):
#    added_count = 0
#
#    def missing():
#        nonlocal added_count  #Stateful closure
#        added_count += 1
#        return 0
#
#    result = defaultdict(missing, current)
#    for key, amount in increments:
#        result[key] += amount
#
#    return result, added_count
#
#result, count = increment_with_report(current, increments)
#print(result)
#assert count == 2

##通过定义类的方式来实现以上闭包实现的功能
#class CountMissing(object):
#    def __init__(self):
#        self.added = 0
#
#    def missing(self):
#        self.added += 1
#        return 0
#
#
#counter = CountMissing()
#result = defaultdict(counter.missing, current)  #Method ref
#
#for key, amount in increments:
#    result[key] += amount
#
#assert counter.added == 2
#print(result)

#更好的方法:定义类中的__call__方法
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
#assert callable(counter)

result = defaultdict(counter, current) #relies on __call__
for key, amount in increments:
    result[key] += amount
print(result)
assert counter.added == 2
