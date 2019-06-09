# -*- coding: UTF-8 -*-

# Filename : helloworld.py
# author by : www.runoob.com

# 该实例输出 Hello World!

import operator
rareList = {}
rareList[1] = 1
print('Hello World!')
print(rareList)
print('get:', rareList[1])
print('if exist:', 21 in rareList)

for i in [1,2,3]:
    print(i)


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
print('length', len(sorted_x))
print(sorted_x[1])

key, value = sorted_x[1]
print(key)