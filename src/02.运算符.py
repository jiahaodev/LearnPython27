# -*- coding:UTF-8 -*-

#算术运算符

a,b,c = 21.0,10.0,0

c = a + b
print(c)

c = a - b
print c

c = a * b
print c

c = a / b
print c

c = a % b
print c

c = a // b
print c

a = 2; b = 3
print a**b

#比较运算符
#  == ， ！= ，>, <, >=, <=

#赋值运算符
#  =  +=   -=  *=  /=  %=  **=  //=


#位运算
#  & | ^ ~  <<  >>
a = -1
b = 011
c = a & b
print c


# 逻辑运算符
# and  or  not


# 成员运算符  (测试是否包含)
#  in  , not in

# 注意： in 判断 list、tuple、string这是没有争议的。
#          如果是判断是否在字典中，则是指是否有该key值。
dic = {"a":111,"b":222}
print "a" in dic
print 111 in dic



# 身份运算符
# is  is not
#is用于判断两个变量引用是否同一个，==用于判断引用变量的值是否相等




