# -*- coding:UTF-8 -*-

print "Python是一个非常棒的语言,不是吗？"

# str = raw_input("请输入：")
# print "你输入的内容是:",str

# str = input("请输入：")
# print "你输入的内容是:",str

#打开一个文件
fo  = open("foo.txt","w")
print "文件名：",fo.name
print "是否已关闭：",fo.closed
print "访问模式：",fo.mode
print "末尾是否强制加空格：",fo.softspace

#关闭打开文件
fo.close()

# 写文件
fo = open("foo.txt","w")
fo.write("www.runoob.com\nVery good site!\n")
fo.close()


# 读文件
fo = open("foo.txt","r+")
str = fo.read(10)
# str = fo.read(12)
print "读取的字符串是：",str
fo.close()

#文件定位

fo = open("foo.txt","r+")
str = fo.read(10)
print "读取的字符串是：",str
#查找当前位置
position = fo.tell()
print "当前文件位置：",position

#把指针再次重新设置到文件开头
position = fo.seek(0,0)
str = fo.read(5)
print "重新读取字符串：",str

fo.close()


# 删除文件
import os
# os.remove("test2.txt")  #如果文件不存在，将会报错

#创建目录test
# os.mkdir("testDir")  #如果目录已经存在，尝试重复创建，也会报错

#删除目录
# os.rmdir("testDir")  #如果目录不存在，尝试重复创建，也会报错


#获取当前工作目录
# print os.getcwd()
#
# os.mkdir("testDir")

#改变当前工作目录
# os.chdir("testDir")
#
# os.mkdir("abc")

