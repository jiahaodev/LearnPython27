# -*- coding:UTF-8 -*-

list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5]
list3 = ['a','b','c','d']

print list1[0]
print list2[1:5]

list = []
list.append('Google')
list.append('Runoob')
print list

del list1[2]
print list1

print len(list3)
print list2 + list3
print list2 * 4
print 3 in list2

for x in list2:
	print x,
print

# 列表函数

aList = [123,'xyz','zara','abc']
aList.append(2009)
print aList
