# -*- coding:UTF-8 -*-

dict = {'a':1,'b':2,'b':3}
print dict['b']

del dict['b']

print dict


dict = {'a':1,'b':2,'c':3}
print str(dict)

print type(dict)

print type([])

# dict.clear()

print dict

dict_copy = dict.copy()
print dict_copy

dict = dict.fromkeys(['a','b'],[1,2])
print dict


dict = {'a':1,'b':2,'c':3}
print dict.get('d',"default")

print dict.has_key('d')

print dict.items()

print dict.keys()
print dict.values()

dict.setdefault('c',30)
dict.setdefault('d',40)

print dict

dict2 = {'e':5,'f':6}
dict.update(dict2)

print dict

var = dict.pop('a')
print var
print dict

print "--start--"

while(len(dict)!=0):
	var = dict.popitem()
	print var

print "--end--"

print dict