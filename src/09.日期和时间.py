# -*- coding:UTF-8 -*-

import time;

ticks = time.time()
print "当前时间戳为：",ticks

localtime = time.localtime(time.time())
print "本地时间为：",localtime

localtime = time.localtime(time.time())
localtime = time.asctime(localtime)
print "本地时间为：",localtime


print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


import calendar
cal = calendar.month(2020,5)
print "2020-05"
print cal

print time.clock()

#睡眠指定的“秒数”
time.sleep(10/100)

print "finish"

print time.time()


cal = calendar.calendar(2020,w =2,l=1,c=20)
# print cal
