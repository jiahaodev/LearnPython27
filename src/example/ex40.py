# -*- coding:UTF-8 -*-

'''
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
'''

a = [1, 2, 3, 4, 5, 6]
N = len(a)
for i in range(N / 2):
    a[i], a[N - 1 - i] = a[N - 1 - i], a[i]

print a
