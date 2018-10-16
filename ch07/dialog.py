#!/usr/bin/env python
# coding=utf-8

# 1===================
#import app
#class Dialog(object):
#    def __init__(self, save_dir):
#        self.save_dir = save_dir
#    # ...
#
#save_dialog = Dialog(app.prefs.get('save_dir'))
#
#def show():
#    print('hello world')


# 2====================
import prefs

class Dialog(object):
    def __init__(self, save_dir):
        self.save_dir = save_dir
    # ...

save_dialog = Dialog(prefs.prefs.get('save_dir'))

def show():
    print('hello world')
