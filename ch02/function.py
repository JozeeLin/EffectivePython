#!/usr/bin/env python3
# coding=utf-8
import json


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result


def decode(data, default={'a':3}):
    try:
        return json.loads(data)
    except ValueError:
        return default

#通过使用动态参数的形式来解决这个问题
def decode(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == '__main__':
#    #第一个函数测试
#    divide(1,0)
#    #第二个函数测试
#    visits = [15,35,80]
#    percentages = normalize(visits)
#    print(percentages)
#
#    #第三个函数测试
#    foo = decode('bad data')
#    foo['stuff'] = 5
#    bar = decode('also bad')
#    bar['meep'] = 1
#    print('FOO:', foo)
#    print('BAR:', bar)

	#第四个函数测试
    foo = decode('bad data')
    foo['stuff'] = 5
    bar = decode('also bad')
    bar['meep'] = 1
    print('Foo:', foo)
    print('Bar:', bar)

