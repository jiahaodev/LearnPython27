# -*- coding:UTF-8 -*-

'''
题目：两个变量值互换。

程序分析：无
'''

def exchage(a,b):
    a,b = b,a
    return (a,b)

x = 10
y = 20
print "x = %d,y = %d" % (x,y)
x,y = exchage(x,y)
print "x = %d,y = %d" % (x,y)
