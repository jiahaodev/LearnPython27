# -*- coding:UTF-8 -*-

import json

data = [{'a':1,'b':2,'c':3}]

json_str = json.dumps(data)

print json_str
print 'type:{0}'.format(type(json_str))

json_data = json.loads(json_str)
print json_data
print 'type:{0}'.format(type(json_data))
