#!/usr/bin/env python
# coding=utf-8


'''
python3 二进制数据和Unicode数据之间的相互转换
'''
def to_str_3(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value  #Instance of str


def to_bytes_3(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str

    return value


'''
python2 二进制数据和Unicode数据之间的相互转换
'''
def to_unicode_2(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value


def to_str_2(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str

    return value
