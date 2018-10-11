#!/usr/bin/env python
# coding=utf-8

import subprocess
import time
import os

# 1=================
#proc = subprocess.Popen(['echo', 'Hello from the child!'],stdout=subprocess.PIPE)
#out, err = proc.communicate() # 用communicate方法读取子进程的输出信息,并等待其终止
#print(out.decode('utf-8'))


# 2=========================
#proc = subprocess.Popen(['sleep','0.3'])
#start = time.time()
#while proc.poll() is None:
#    print('Working...')
#end = time.time()
#print('Finished in %.3f seconds' % (end-start))
#print('Exit status', proc.poll())


# 3==========================
def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

#start = time.time()
#procs = []
#for _ in range(10):
#    proc = run_sleep(0.1)
#    procs.append(proc)
#
##然后通过communicate方法,等待这些子进程完成其I/O工作并终结
#for proc in procs:
#    proc.communicate()
#end = time.time()
#print('Finished in %.3f seconds' % (end-start))


# 4===========================
def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Q13S\x11'
    proc = subprocess.Popen(
        ['openssl','enc','-des3','-pass','env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()  # Ensure the child gets input
    return proc


# 4========================
#procs = []
#for _ in range(3):
#    data = os.urandom(10)
#    proc = run_openssl(data)
#    procs.append(proc)
#
#for proc in procs:
#    out, err = proc.communicate()
#    print(out[-10:])


# 5===========================
#def run_md5(input_stdin):
#    proc = subprocess.Popen(
#        ['md5sum'],
#        stdin = input_stdin,
#        stdout=subprocess.PIPE
#    )
#    return proc
#'''
#现在启动一套openssl进程,以便加密某些数据,同时启动另一套md5进程,以便根据加密后的输出内容来计算其哈希码
#'''
#input_procs = []
#hash_procs = []
#for _ in range(3):
#    data = os.urandom(10)
#    proc = run_openssl(data)
#    input_procs.append(proc)
#    hash_proc = run_md5(proc.stdout)
#    hash_procs.append(hash_proc)
#
#for proc in input_procs:
#    proc.communicate()
#
#for proc in hash_procs:
#    out, err = proc.communicate()
#    print(out.strip())


# 6================================
proc = run_sleep(10)
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()
print('Exit status', proc.poll()) #输出子进程的退出状态
