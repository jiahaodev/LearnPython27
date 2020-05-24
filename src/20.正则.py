# -*- coding:UTF-8 -*-

import re

## match 方法
print(re.match("www","www.runoob.com").span()) #在起始位置匹配
print(re.match("com","www.runoob.com"))

## group 、 groups 方法
line = "Cats are smarter than dogs"
matchObj = re.match(r"(.*) are (.*?) .*", line, re.M|re.I)

if matchObj:
	print "mathchObj.group():",matchObj.group()
	print "mathchObj.group(1):",matchObj.group(1)
	print "mathchObj.group(2):",matchObj.group(2)
	print "mathchObj.groups():",matchObj.groups()
else:
	print "No match!!"

## search
# re.match只匹配字符串的[开始]，如果字符串开始不符合正则表达式，
#                            则匹配失败，函数返回None；
# 而re.search匹配[整个字符串]，直到找到一个匹配。

matchObj = re.match(r'dogs',line,re.M|re.I)
if matchObj:
	print "match --> matchObj.group():",matchObj.group()
else:
	print "No match!!"

searchObj = re.search(r"dogs",line,re.M|re.I)
if searchObj:
	print "search --> searchObj.group():",searchObj.group()
	# print "search --> searchObj.group(1):",searchObj.group(1)
else:
	print "No search!!"


## 检索 和 替换
phone = "2004-959-559 #这是一个国外电话号码"

#删除字符串中的Python注释
num = re.sub(r"#.*$","",phone)
print "电话号码是:",num

#删除所有非数字(-)的字符串
num = re.sub(r"\D","",phone)
print "电话号码是:",num


#将匹配的数字交给函数处理
def double(matched):
	value = int(matched.group('value'))
	return str(value*2)

s = "A23G4HFD567"
print(re.sub('(?P<value>\d+)',double,s))


## compile函数
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print m
m = pattern.match('one12twothree34four',2,10)
print m
m = pattern.match('one12twothree34four',3,10)
m = pattern.match('one12twothree34four',3)
print m
if m != None:
	print m.group(0)
	print m.start(0)
	print m.end(0)
	print m.span(0)


## findall
pattern = re.compile(r"\d+")
result1 = pattern.findall('runoob 123 goole 456')
result2 = pattern.findall('run8800b123goole456',0,10)

print result1
print result2


## finditer
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
	print(match.group())




















