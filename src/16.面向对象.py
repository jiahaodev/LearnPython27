# -*- coding:UTF-8-*-


# 定义类

class Employee:
	'所有员工的基类'

	empCount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name:",self.name,",Salary:",self.salary


# 创建实例对象
emp1 = Employee('Zara',2000)
emp2 = Employee('Manni',5000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.age = 7
emp1.age = 8

print emp1.age
# del emp1.age

print getattr
print hasattr(emp1,'age')
print setattr(emp1,'new_age',3)

print emp1.new_age
delattr(emp1,'new_age')
print getattr(emp1,'new_age',"000")


print "Total Employee %d" % Employee.empCount

# python 内置属性
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

class Test:
	def prt(self):
		print(self)
		print(self.__class__)

# t = Test()
# t.prt()


## 垃圾回收
# 析构函数
class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name,"销毁"

pt1 = Point()
pt2 = pt1
pt3 = pt1

print id(pt1),id(pt2),id(pt3)
print 111
del pt1
print 222
del pt2
# print 333
# del pt3

print "aaa"



##  类的继承
class Parent:
	parentAttr = 100
	def __init__(self):
		print "调用父类构造函数"

	def parentMethod(self):
		print "调用父类方法"

	def myMethod(self):
		print "父类：myMethod"

	def setAttr(self,attr):
		Parent.parentAttr = attr

	def getAttr(self):
		print "父类属性：",Parent.parentAttr

class Child(Parent):
	def __init__(self):
		print "调用子类构造函数"

	def childMethod(self):
		print "调用子类方法"

	def myMethod(self):
		print "子类：myMethod"

c = Child()
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值
c.myMethod()

print c.__init__
# print c.__del__
# print c.__repr__(c)
# ?print c.__str__(c)
# print c.__cmp__(c)




## 运算符重载
class Vector:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector(%d,%d)' % (self.a,self.b)

	def __add__(self,other):
		return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2









