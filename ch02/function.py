#!/usr/bin/env python3
# coding=utf-8
#def divide(a,b):
#    try:
#        return a/b
#    except ZeroDivisionError as e:
#        raise ValueError('Invalid inputs') from e
#
#divide(1,0)

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

visits = [15,35,80]
percentages = normalize(visits)
print(percentages)
