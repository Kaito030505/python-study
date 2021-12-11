# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:40:09 2021

@author: USER
"""

test_dict_1={'YEAR':'2021','MONTH':'12','DAY':'07'}
print(test_dict_1)

print('----------------------')

print(test_dict_1['YEAR'])
print(test_dict_1.get('YEAR'))
print(test_dict_1.get('YEARS'))

print('---------------------')

print(test_dict_1.get('YEAR','NOT FOUND'))
print(test_dict_1.get('YEARS','NOT FOUND'))
print(test_dict_1.get('?'))
test_dict={}

test_dict[1]='Hello'
test_dict[2]='How are you?'

print(test_dict)
#del test_dict[1]
print(test_dict)

print(test_dict_1.keys())
print(test_dict_1.values())

for x,y in test_dict.items():
    print(x,y)

print('YEAR' in test_dict_1)
print('YEARS' in test_dict_1)

test_set={'python','-','izm','-','com'}
print(test_set)

print('---------------------------')

for x in test_set:
    print(x)
    
number_list=[1,2,3,4,5,6,7,8,9,10]
print(number_list[:])
print(number_list[::])
print(number_list[:-1:2])
print(number_list[1:8:2])

