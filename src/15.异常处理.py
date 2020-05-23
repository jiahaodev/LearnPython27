# -*- coding:UTF-8 -*-

def temp_convert(var):
	try:
		return int(var)
	except ValueError,Argument:
		print "参数没有包含数字\n",Argument
	# else:
	# 	print "else do"
	finally:
		print "finally do"

temp_convert("xyz")
temp_convert("20")


# 触发异常

def functionName(level):
	try:
		if level < 1:
			raise Exception("Invalid level!",level)
		else:
			print("ok,level:",level)
		print("finish")
	except Exception,Argument:
		print Argument


functionName(0)
functionName(2)


#用户自定义异常
class Networkerror(RuntimeError):
	def __init__(self,arg):
		self.args = arg

try:
	raise Networkerror("Bad hostname")
except Networkerror,e:
	print e.args
