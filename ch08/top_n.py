#!/usr/bin/env python
# coding=utf-8

import tracemalloc
tracemalloc.start(10)  # save up to 10 stack frames

time1 = tracemalloc.take_snapshot()
a = 1
b = a
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)
