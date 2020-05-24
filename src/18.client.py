# -*- coding:UTF-8 -*-

'''
import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
str = s.recv(1024)
str=str.decode('utf-8').encode("gbk")  # 修改编码，方便查看
print str

s.close()

'''


import sys
reload(sys)
sys.setdefaultencoding('utf8')
import socket# 客户端 发送一个数据，再接收一个数据
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
client.connect(('localhost',9090)) #建立一个链接，连接到本地的9090端口

while True:
	msg = "客户端：欢迎访问菜鸟教程！"
	client.send(msg.encode('utf-8'))
	data = client.recv(1024)
	print('recv:',data.decode('utf-8'))
	client.close()
	break







