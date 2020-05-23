# -*-coding:UTF-8 -*-

#数学库
import math

print abs(-10)
print math.ceil(4.1)
print cmp(10,8)

print round(1.23456)


# 随机数
import random

print random.choice([99,1,2,3,4])
print random.choice('python')
print random.randrange(1,10,2)
print random.random()
list = [1,2,3,4,5]
random.shuffle(list)
print list
print random.uniform(10,20)

print math.pi
print math.e

print math.sin(math.pi/2)
print math.cos(0)
print math.tan(math.pi/4)

print math.asin(1)/math.pi
print math.acos(0)/math.pi
print math.atan(1)/math.pi

print math.degrees(math.pi/2)
print math.radians(90)/math.pi
print math.hypot(3,4)

