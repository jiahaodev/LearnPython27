# -*- coding:UTF-8 -*-

g_str = "全局字符串"

def printme(str):
	"打印传入的字符串到标准显示设备上"
	print str
	return

def globalTest():
	print g_str
	pass

printme("中文")

globalTest()


#关键字参数
def printinfo(name,age):
	print "Name:",name
	print "Age:",age

printinfo(age = 100,name = "小米")

#默认参数
def printinfo2(name,age = 35):
	print "Name:",name
	print "Age:",age

printinfo2(age = 30,name = "x")
printinfo2(name = "x")

#不定长参数
def printinfo3(arg1,*vartuple):
	print "输出："
	print arg1
	for var in vartuple:
		print var
	return

printinfo3(10)
printinfo3(10,20,30,40,50)


#lambda函数
sum = lambda arg1,arg2: arg1+arg2

print sum(10,20)
print sum(30,30)


#全局变量，局部变量
total = 100

def sum2(arg1,arg2):
	global total
	total = arg1 + arg2
	return total

print sum2(3,4)
print total
