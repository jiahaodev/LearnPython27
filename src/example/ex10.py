# -*- coding:UTF-8 -*-

'''
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
'''

import time

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

time.sleep(1)

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))