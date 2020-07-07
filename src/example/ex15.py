# -*- coding:UTF-8 -*-

'''
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，
60分以下的用C表示。


'''

sorce = int(raw_input("输入分数：\n"))

if sorce >= 90:
    grade = 'A'
elif sorce >= 60:
    grade = 'B'
else:
    grade = 'C'
print "%d 属于 %s" % (sorce,grade)
