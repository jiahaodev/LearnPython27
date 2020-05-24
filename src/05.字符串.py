# -*- coding:UTF-8 -*-

var1 = "Hello World!"
var2 = "Python Runoob"

print "var1[0]:",var1[0]
print "var2[1:5]",var2[1:5]

print "输出：- ",var1[:6] + "Runoob!"


## python 字符串运算符
a = "Hello"
b = "Python"

print "a+b:",a+b
print "a*2:",a*2
print "a[1]:",a[1]
print "a[1:4]:",a[1:4]

if("H" in a):\
	print "H在变量a中"
else:
	print "H不在变量a中"

if("M" not in a):
	print "M not in var a"
else:
	print "M in var a"

print r'\nabc\nabc'
print R'\nabc\nabc'

## python 字符串格式化
print "My name is %s and weight is %d kg!" % ('Zara',21)

# formart格式化h函数
print "{} {}".format("Hello","world")

print "{1} {0} {1}".format("hello","world")

#通过字典设置参数
print("网站名:{name},地址{url}".format(name = '菜鸟教程',url = 'www.runoob.com'))

site = {"name":"菜鸟教程", "url":"www.runoob.com"}
print("网站名:{name},地址{url}".format(**site))

my_list = ['菜鸟教程','www.runoob.com']
print("网站名:{0[0]},地址{0[1]}".format(my_list))

#str.format() 传入对象
class AssignValue(object):
	def __init__(self,value):
		self.value = value

my_value = AssignValue(6)
print('value为:{0.value}'.format(my_value))
print('value为:{.value}'.format(my_value))  # 0 是可选的


## python 的字符串内建函数
a = "a,babc"
b = " a,b"

print a.capitalize()
print b.capitalize()
print a.center(20)
print a.count("b")


str = "this is string example...wow!!!"
str2 = str.encode('base64','strict')
print "Encoded String:",str2
print "Decoded String:",str2.decode('base64','strict')

print str.endswith("w!!!")

print str.find("string")
print str.index("string")

str = "-"
seq = ("a","b","c")
print str.join(seq)
seq2 = ["a","b","c"]
print str.join(seq2)

from string import maketrans
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab,outtab)

str = "this is string example...wow!!!"
print str.translate(trantab)


str = "ABCXY this is really a string example....wow!!!"
print "Max character: " + max(str)

str = "ABCXYthisisastringexamplewow"
print "Min character: " + min(str)