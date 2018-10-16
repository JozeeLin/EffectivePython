#!/usr/bin/env python
# coding=utf-8
import gc
found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))

a = 1
b = a

found_objects = gc.get_objects()
print('%d objects after' % len(found_objects))
for obj in found_objects[:3]:
    print(repr(obj)[:100])
