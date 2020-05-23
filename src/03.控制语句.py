# -*- coding:UTF-8 -*-


#条件语句
flag = False
name = 'luren'
if name == 'python':
	flag = True
	print 'welcome boss'
else:
	print name

num = 5
if num == 3:
	print 'boss'
elif num == 2:
	print 'user'
elif num == 1:
	print 'worker'
elif num < 0:
	print 'error'
else:
	print 'roadman'

#循环语句
#while 语句
a = 1
while a < 10:
	print a
	a += 2

numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) > 0:
	number = numbers.pop()
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)

print even
print odd

i = 1
while i < 10:
	i += 1
	if i%2 > 0:
		continue
	print i

i = 1
while 1:
	print i
	i += 1
	if i > 10:
		break

#无限循环，暂时屏蔽
# var = 1
# while var == 1:
# 	var = raw_input("Enter a number:")
# 	print "You entered:",var
#
# print "Good bye!"

count  = 0
while count < 5:
	print count," is less than 5"
	count += 1
else:
	print count," is not less than 5"



# for 循环语句
for letter in 'Python':
	print '当前字母：',letter

fruits = ['banana','apple','mango']
for fruit in fruits:
	print '当前水果：',fruit


print "len:",len(fruits)
print "range:",range(3)

for index in range(len(fruits)):
	print '当前水果：',fruits[index]


# 循环嵌套
i = 2
while(i<100):
	j = 2
	while(j<=(i/j)):
		if not(i%j): break
		j = j + 1
	if (j > i/j): print i," 是素数"
	i = i + 1


# break 语句

# continue 语句

# pass 语句

for letter in 'python':
	if letter == 'h':
		pass
		print '这是pass块'
		pass
	print '当前字母：',letter











