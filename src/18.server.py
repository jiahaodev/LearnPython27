# -*- coding:UTF-8 -*-

'''
import socket

s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)

while True:
	c,addr = s.accept()
	print '连接地址:',addr
	c.send('欢迎访问菜鸟教程！')
	c.close()

'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import socket
#建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9090))
server.listen(5)

while True:
	conn,addr = server.accept()
	data = conn.recv(1024)
	print('receive:',data.decode("utf-8"))
	print('data:',data)
	conn.send(data.encode("utf-8"))
	conn.close()
