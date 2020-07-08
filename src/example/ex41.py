# -*- coding:UTF-8 -*-

'''
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
'''


def varfunc():
    var = 0
    print "var = %d" % var
    var += 1


for i in range(3):
    varfunc()

# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print self.StaticVar


print Static.StaticVar

a = Static()
for i in range(3):
    a.varfunc()