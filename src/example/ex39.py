# -*- coding:UTF-8 -*-

'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况
，插入后此元素之后的数，依次后移一个位置。
'''

a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
print '原始列表:'
for i in range(len(a)):
    print a[i]

number = int(raw_input("\n插入一个数字：\n"))

end = a[-1]

if number > end:
    a.append(number)
else:
    for i in range(len(a)):
        if a[i] > number:
            temp1 = a[i]
            a[i] = number
            for j in range(i+1,len(a) + 1):
                if j == len(a):
                    a.append(end)
                else:
                    temp2 = a[j]
                    a[j] = temp1
                temp1 = temp2
            break

for i in a:
    print i
